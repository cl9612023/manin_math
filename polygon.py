from manim import *
from datetime import datetime

today_date = datetime.now().strftime("%Y_%m_%d")

config.output_file = f"Polygon_{today_date}.mp4"
config.media_dir = "/media/sf_share/manim_learning"

class Polygon(Scene):
    def construct(self):
        self.camera.background_color = WHITE #背景顏色
        pentagon = RegularPolygon(n=5) #五邊形
        pentagon.set_stroke(BLACK,width=5)
        pentagon.set_fill(YELLOW,opacity=1)
        vertices  = pentagon.get_vertices()
        point_1 = Dot(point=vertices[0], color=BLACK)
        self.play(Create(pentagon))
        self.add(point_1)
        self.wait(1)
