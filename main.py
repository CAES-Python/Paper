from kivy.app import App


from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class SampleApp(App):
	def build(self):
		Box=BoxLayout()
		b=Button(text='Hello',font_size=20)
		Box.add_widget(b)
		return Box
# Run the program
if __name__ == "__main__":
	SampleApp().run()
