"""
Dynamic Labels kivy program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

__author__ = "Rory Reid"


class DynamicLabelsApp(App):
    """Main Program - Kivy app that uses dynamic labels"""

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ["Rory", "Lindsay", "Olivia", "Frank", "Tyrone", "Rebecca", "Julie", "Leo", "Luna"]

    def build(self):
        """Builds the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from a list of names"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
