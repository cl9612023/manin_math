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
        self.play(Create(pentagon))
        self.wait(1)
