from kivymd.app import MDApp
from kivy_garden.mapview import MapView
from kivy.core.window import Window



class MapViewApp(MDApp):

    def build(self):
        # Window.size = (1200, 890)
        mapview = MapView(zoom=10, lat=36, lon=-115)
        return mapview
        

MapViewApp().run()