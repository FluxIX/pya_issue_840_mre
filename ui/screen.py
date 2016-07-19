from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string(
   """
<MainScreen>
   Label:
      text: "This runs on Linux but fails on Android."
   """
   )

class MainScreen( Screen ):
   pass
