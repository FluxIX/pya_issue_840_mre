from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

# from ui.screen import MainScreen # This line works on Android but not Linux
from .ui.screen import MainScreen # This line works on Linux but not Android

class MreApp( App ):
   def build( self ):
      screens = [ MainScreen() ]

      manager = ScreenManager()

      for screen in screens:
         manager.add_widget( screen )

      return manager

def run_app( args = None ):
   app = MreApp( title = "p4a Issue #840 MRE" )
   app.run()
