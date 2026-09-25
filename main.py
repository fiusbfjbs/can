from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

# 全屏浅绿色背景 (light green = #90EE90)
Window.clearcolor = (144 / 255, 238 / 255, 144 / 255, 1)


class GreenCanvas(Widget):
    pass


class GreenCanvasApp(App):
    def build(self):
        return GreenCanvas()


if __name__ == "__main__":
    GreenCanvasApp().run()
