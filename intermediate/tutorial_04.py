from manim import *

class CodeFromString(Scene):
    def construct(self):
        code = '''from manim import Scene, Square

class FadeInSquare(Scene):
    def construct(self):
        s = Square()
        self.play(FadeIn(s))
        self.play(s.animate.scale(2))
        self.wait()
'''
        rendered_code = Code(
            code_string=code, tab_width=4, background="window",
            language="python", paragraph_config=dict(font="Monospace")
        )
        self.play(Write(rendered_code))
        self.wait(2)
