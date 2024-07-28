from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicLabelsApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        names = ["Alice", "Bob", "Charlie", "David"]
        for name in names:
            self.ids.main.add_widget(Label(text=name))

class DynamicLabelsAppApp(App):
    def build(self):
        return DynamicLabelsApp()

if __name__ == "__main__":
    DynamicLabelsAppApp().run()
