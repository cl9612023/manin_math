from manim import *

config.media_dir = "/media/sf_share/manim_learning"

class Polygon(Scene):
    def construct(self):
        pentagon = RegularPolygon(n=5)
        self.play(Create(pentagon))
        self.wait(1)
