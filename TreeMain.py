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
        blue = Circle(radius=0.25, color = OFFBLACK, fill_color = BLUE, fill_opacity = 0.9)
        green = Circle(radius=0.25, color = OFFBLACK, fill_color = GREEN, fill_opacity = 0.9)
        red = Circle(radius=0.25, color = OFFBLACK, fill_color = RED, fill_opacity = 0.9)
        yellow = Circle(radius=0.25, color = OFFBLACK, fill_color = YELLOW, fill_opacity = 0.9)
        orange = Circle(radius=0.25, color = OFFBLACK, fill_color = ORANGE, fill_opacity = 0.9)
        purple = Circle(radius=0.25, color = OFFBLACK, fill_color = PURPLE, fill_opacity = 0.9)
        black = Circle(radius=0.25, color = OFFBLACK, fill_color = OFFBLACK, fill_opacity = 0.9)

        tree = TreeController(blue)
        tree.insert(green, [0])
        tree.insert(red, [1])
        tree.insert(yellow, [0, 0])
        tree.insert(orange, [0, 1])
        tree.insert(purple, [1, 0])
        tree.insert(black, [1, 0, 0])
        tree.autoPosition(vertical_spacing = 0.1)

        self.play(Write(tree.mobject))

        self.play(FadeOut(tree.subtree([0]).mobject))