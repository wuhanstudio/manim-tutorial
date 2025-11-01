from manim import *

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square

        # transform the square into a circle
        self.play(Transform(square, circle))

        # color the circle on screen
        self.play(square.animate.set_fill(PINK, opacity=0.5)) 
