from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SquaringApp(BoxLayout):
    def handle_square(self):
        try:
            number = int(self.ids.input_number.text)
            self.ids.output_label.text = str(number ** 2)
        except ValueError:
            self.ids.output_label.text = "Invalid input"

class SquaringAppApp(App):
    def build(self):
        return SquaringApp()

if __name__ == "__main__":
    SquaringAppApp().run()
