from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutDemo(BoxLayout):
    def handle_greet(self):
        name = self.ids.input_name.text
        self.ids.output_label.text = f"Hello, {name}!"

    def handle_clear(self):
        self.ids.input_name.text = ''
        self.ids.output_label.text = ''

class BoxLayoutDemoApp(App):
    def build(self):
        return BoxLayoutDemo()

if __name__ == "__main__":
    BoxLayoutDemoApp().run()
