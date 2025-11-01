from manim import *

class TextDemo(Scene):
    def construct(self):
        # create a text object
        t = Text("Hello, Manim!", color=DARK_BLUE, weight=BOLD, font_size=100) 
        
        # show the text on screen
        self.play(Write(t))  

        # wait for a second before ending the scene
        self.wait(3)  
        self.play(Unwrite(t))
