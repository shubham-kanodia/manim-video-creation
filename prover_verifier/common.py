from manim import *


class Bubble(SVGMobject):
    file_name: str = "Bubbles_speech.svg"

    def __init__(
        self,
        direction=LEFT,
        center_point=ORIGIN,
        content_scale_factor: float = 0.7,
        height=4.0,
        width=8.0,
        max_height=None,
        max_width=None,
        bubble_center_adjustment_factor=0.125,
        fill_color=BLACK,
        fill_opacity=0.8,
        stroke_color=WHITE,
        stroke_width=3.0,
        **kwargs
    ):
        self.direction = direction
        self.bubble_center_adjustment_factor = bubble_center_adjustment_factor
        self.content_scale_factor = content_scale_factor

        super().__init__(
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_color=stroke_color,
            stroke_width=stroke_width,
            **kwargs
        )

        self.center()
        self.set_height(height, stretch=True)
        self.set_width(width, stretch=True)
        if max_height:
            self.set_max_height(max_height)
        if max_width:
            self.set_max_width(max_width)
        if direction[0] > 0:
            self.flip()

        self.content = Mobject()
