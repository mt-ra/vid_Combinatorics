from manim import *

# THIS CREATES A STATIC TREE
# THERE ARE NO INSERTION ANIMATIONS
# THE EDGES ARE NOT UPDATED TO ATTACH TO THE NDOES

class Subtree:
    def __init__(self, mobject : VMobject):
        self.root_mobject : VMobject = mobject
        self.mobject : VGroup = VGroup(mobject)
        self.children : List[Subtree] = []
        self.parent : Subtree = None
        self.edge_to_parent : Line = None

    def height(self) -> float:
        return self.mobject.get_height()

    def width(self) -> float:
        return self.mobject.get_width()

    # for easier access of subtrees
    def subtree(self, path : List[int]) -> "Subtree":
        if len(path) == 0:
            return self
        elif (path[0] < 0 or len(self.children) <= path[0]):
            print("ERROR: INDEX OUT OF RANGE")
        else:
            return self.children[path[0]].subtree(path[1:])

    def insert(self, item : VMobject, path : List[int]):
        if len(path) == 0:
            print ("ERROR: EMPTY INSERTION PATH")
        elif (path[0] < 0 or len(self.children) < path[0]):
            print("ERROR: INDEX OUT OF RANGE")
        elif len(path) == 1:
            newitem = Subtree(item)
            newitem.parent = self
            self.children.insert(path[0], newitem)
            self.mobject.add(newitem.mobject)
        else:
            self.children[path[0]].insert(item, path[1:])

    def autoPosition(self, v : float, h : float):
        if len(self.children) == 0:
            return
        else:
            # autoPosition the internals of each child
            for c in self.children:
                c.autoPosition(v, h)
            
            # find the widths of all the children
            childCount = len(self.children)
            child_widths = []
            child_width_sum = 0
            for c in self.children:
                child_widths.append(c.mobject.get_width())
                child_width_sum += c.mobject.get_width()
            
            # use these to find the positions relative to the parent
            # such that the parent is in the centre
            total_width = (childCount - 1) * h + child_width_sum
            curr_left_border = -total_width/2
            subtreePositions = []
            for w in child_widths:
                subtreePositions.append(curr_left_border + w/2)
                curr_left_border += h + w

            # now position the children relative to the parent
            for p, c in zip(subtreePositions, self.children):
                height = c.height()
                c.mobject.move_to(self.root_mobject.get_bottom() + DOWN*height/2 + v*DOWN + p*RIGHT)

    

class TreeController:
    def __init__(self, root : VMobject):
        self.root = Subtree(root)
        # the thing that is actually displayed
        self.mobject : VMobject = self.root.mobject
        self.all : List[Subtree] = [self.root]

    # NON-ANIMATION METHODS

    def subtree(self, path : List[int]) -> Subtree:
        return self.root.subtree(path)

    def insert(self, item : VMobject, path : List[int]):
        self.root.insert(item, path)
        self.all.append(self.subtree(path))

    def autoPosition(self, **kwargs):
        v = kwargs.get("v", 0.5)
        h = kwargs.get("h", 0.2)
        self.root.autoPosition(v, h)

    def addEdges(self, **kwargs):
        for st in self.all:
            if st.parent != None:
                edge = Line(
                    st.parent.root_mobject.get_bottom(),
                    st.root_mobject.get_top(), 
                    **kwargs
                )
                st.parent.mobject.add(edge)
                st.edge_to_parent = edge

                # we want to shorten

                edge.scale(0.6)