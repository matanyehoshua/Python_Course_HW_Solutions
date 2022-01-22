
#importing stuff to run Kivy
import kivy
from kivy.app import App
from kivy.uix.label import Label


# building the OOP class
class MyApp(App):
    def build(self):
        return Label(text="Hello world")

# running the app
if __name__ == "__main__":
    MyApp().run()