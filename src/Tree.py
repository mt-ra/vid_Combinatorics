from manim import *


# Each subtree gets a horizontal span that depends on the number of leaves it has

class Subtree:
    def __init__(self, mobject : VMobject):
        self.root_mobject : VMobject = mobject
        self.mobject : VGroup = VGroup(mobject)
        self.children : List[Subtree] = []

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
            childWidths = []
            totalWidth = 0
            for c in self.children:
                childWidths.append(c.mobject.get_width())
                totalWidth += c.mobject.get_width()
            
            # use these to find the positions relative to the parent
            # such that the parent is in the centre
            total_width = childCount 
            
            # now position the children relative to the parent
            counter = 0
            for c in self.children:
                width = c.width()
                height = c.height()
                c.mobject.move_to(self.root_mobject.get_bottom() + DOWN*height/2 + v*DOWN + counter*RIGHT)
                counter += 1


class TreeController:
    def __init__(self, root : VMobject):
        self.root = Subtree(root)
        # the thing that is actually displayed
        self.mobject = self.root.mobject

    # NON-ANIMATION METHODS

    def subtree(self, path : List[int]) -> Subtree:
        return self.root.subtree(path)

    def insert(self, item : VMobject, path : List[int]):
        self.root.insert(item, path)

    def autoPosition(self, **kwargs):
        v = kwargs.get("vertical_spacing", 1)
        h = kwargs.get("horizontal_buffer", 0.1)
        self.root.autoPosition(v, h)

    # ANIMTION METHODS (returns an animation object)


