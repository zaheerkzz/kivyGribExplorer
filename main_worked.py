from kivy.app import App
from kivy_garden.mapview import MapView
import xarray as xr
import matplotlib.pyplot as plt
# from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        # label = Label(text='Hello from Kivy',
        #               size_hint=(.5, .5),
        #               pos_hint={'center_x': .5, 'center_y': .5})

        # return label
        file_path = 'grb/ww3_wind_1.grb'

        ds = xr.load_dataset(file_path, engine="cfgrib")
        ds = ds - 273.15
        ds.sst[0].plot(cmap=plt.cm.coolwarm)
        mapview = MapView(zoom=10, lat=36, lon=-115, cls=plt.gcf())
        return mapview

if __name__ == '__main__':
    app = MainApp()
    app.run()