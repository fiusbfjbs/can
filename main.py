import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, Line

# 黑色背景
Window.clearcolor = (0, 0, 0, 1)


class RainbowCanvas(Widget):
    rainbow_colors = [
        (1, 0, 0, 1),      # red
        (1, 0.5, 0, 1),    # orange
        (1, 1, 0, 1),      # yellow
        (0, 1, 0, 1),      # green
        (0, 0.5, 1, 1),    # blue
        (0.5, 0, 1, 1),    # purple
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.draw_rainbow()
        self.bind(pos=self.draw_rainbow, size=self.draw_rainbow)

    def draw_rainbow(self, *args):
        self.canvas.clear()
        with self.canvas:
            x, y = self.center_x, self.center_y
            heading = 0
            size = 30
            angle = 0
            shift = 1

            for i in range(100):
                Color(*self.rainbow_colors[i % len(self.rainbow_colors)])

                rad = math.radians(heading)
                circle_x = x - size * math.sin(rad)
                circle_y = y + size * math.cos(rad)
                Line(circle=(circle_x, circle_y, size), width=4)

                heading -= angle
                rad = math.radians(heading)
                x += shift * math.cos(rad)
                y += shift * math.sin(rad)

                size += 5
                angle += 1
                shift += 1


class RainbowCanvasApp(App):
    def build(self):
        return RainbowCanvas()


if __name__ == "__main__":
    RainbowCanvasApp().run()
