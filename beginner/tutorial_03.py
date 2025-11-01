from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        square = Square()  # create a square

        # set color and transparency
        circle.set_fill(PINK, opacity=0.5)

        # rotate a certain amount
        square.rotate(PI / 4)  

        # animate the creation of the square
        self.play(Create(square))  
        
        # interpolate the square into the circle
        self.play(Transform(square, circle))  

        # fade out animation
        self.play(FadeOut(square))  
