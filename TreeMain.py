from manim import *

from src.Tree import *

OFFBLACK : str = "#111111"
OFFWHITE : str = "#EEEEEE"

class Main(Scene):
    def construct(self):
        # visual setup
        plane = NumberPlane(color = OFFBLACK)
        self.add(plane)
        self.camera.background_color = OFFWHITE

        # TEXT EXAMPLE
        blue = Text("blue", color = OFFBLACK)
        green = Text("green", color = OFFBLACK)
        red = Text("red", color = OFFBLACK)
        yellow = Text("yellow", color = OFFBLACK)
        orange = Text("orange", color = OFFBLACK)
        purple = Text("purple", color = OFFBLACK)
        black = Text("black", color = OFFBLACK)

        tree = TreeController(blue)
        tree.insert(green, [0])
        tree.insert(red, [1])
        tree.insert(yellow, [0, 0])
        tree.insert(orange, [0, 1])
        tree.insert(purple, [1, 0])
        tree.insert(black, [1, 0, 0])

        # setting the position and shit
        tree.mobject.shift(3*UP)
        tree.autoPosition(v=1, h=0.5)
        tree.addEdges(color = OFFBLACK)

        self.play(Write(tree.mobject))

        self.play(FadeOut(tree.subtree([0]).mobject))