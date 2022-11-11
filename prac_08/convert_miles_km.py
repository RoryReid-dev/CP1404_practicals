"""
CP1404 Practical
convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """Kivy app for convert miles to KM"""
    conversion_result = StringProperty()

    def build(self):
        """Build Kivy app"""
        self.title = "Miles to KM Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def calculate_input(self, value):
        """Handle conversion"""
        converted_number = float(value) * MILES_TO_KM
        self.conversion_result = str(f"{converted_number:.2f}")

    def handle_increment(self, value, change):
        """Handle up/down button press"""
        result = float(value) + change
        self.root.ids.input_miles.text = str(f"{result:.2f}")
        self.calculate_input(result)


MilesConverterApp().run()
