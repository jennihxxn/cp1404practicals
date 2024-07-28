from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class ConvertMilesKmApp(BoxLayout):
    result = StringProperty("")

    def handle_convert(self):
        try:
            miles = float(self.ids.input_miles.text)
            self.result = str(miles * 1.60934)
        except ValueError:
            self.result = "0.0"

    def handle_increment(self, value):
        try:
            miles = float(self.ids.input_miles.text)
        except ValueError:
            miles = 0.0
        self.ids.input_miles.text = str(miles + value)
        self.handle_convert()

class ConvertMilesKmAppApp(App):
    def build(self):
        return ConvertMilesKmApp()

if __name__ == "__main__":
    ConvertMilesKmAppApp().run()
