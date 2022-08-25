from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
# from kivy.core.window import Window
from kivy.utils import platform


import numpy as np
# import xarray as xr
import matplotlib.pyplot as plt
import pygrib
import cartopy.crs as ccrs
import cartopy.feature as cfeature
# from kivy_garden.mapview import MapView
import cfgrib


# https://www.youtube.com/watch?v=83C4tl8scoY
class Matty(FloatLayout):
    start_point = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Window.size = (900, 990)

        # path to file 
        # file_path = 'grb/ww3_wind_1.grb'
        file_path = 'grb/dd/gfs1deg_wind_7.grb'
        # file_path = 'grb/dd/gfs_wind_7.grb'

        # open file using pygrib
        self.grbs = pygrib.open(file_path)
        # load GRIB data into xarray
        # self.ds = xr.load_dataset(file_path, engine="cfgrib")

        box = self.ids.box
        # gcf -< get current fiugure
        # box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        box.add_widget(FigureCanvasKivyAgg(self.generate_map_image(self.start_point)))

    def generate_map_image(self, index):
        # close all open windows
        plt.close('all')
        # draw map from GRIB data
        # for count, grb in enumerate(self.grbs):
        try:
            grb = self.grbs[index]
        except OSError:
            grb = self.grbs[1]
            self.start_point=1
        lats, lons = grb.latlons()

        # wind direction
        grb_uwind = grb #U 10m wind component for 2012-03-26 @00UTC
        grb_vwind = grb #V 10m wind component for 2012-03-26 @00UTC
        data_uwind = grb_uwind.values #U 10m wind values in m/s
        data_vwind = grb_vwind.values #V 10m wind values in m/s

        map_crs = ccrs.PlateCarree(central_longitude=0.0, globe=None)

        data_crs = ccrs.PlateCarree()
        # fig = plt.figure(figsize=[100, 40])
        plt.figure(figsize=(16, 22))
        ax = plt.subplot(1, 1, 1, projection=map_crs)
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.coastlines(resolution='110m')
        ax.add_feature(cfeature.LAND)
        ax.add_feature(cfeature.OCEAN)
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.BORDERS, linestyle=':')
        ax.add_feature(cfeature.LAKES, alpha=1)
        ax.add_feature(cfeature.RIVERS)
        # ax.gridlines()

        # ax.set_extent([-130, -72, 20, 55], data_crs)

        ax.gridlines(draw_labels=True, alpha=0.6)
        
        # add grb values
        cntr = ax.contourf(lons, lats, grb.values, transform=data_crs)

        # fig.colorbar(cntr, extend='both', orientation="horizontal",fraction=0.05, shrink=0.5)
        # fig.colorbar(cntr, label='Brightness Temperature (K)')
        # ax.set_aspect('equal')

        # plt.colorbar(cntr, orientation='horizontal', shrink=0.5)
        a_barbs =6
        # ax.barbs(lons[::a_barbs,::a_barbs],lats[::a_barbs,::a_barbs],data_uwind[::a_barbs,::a_barbs], data_vwind[::a_barbs,::a_barbs], transform=ccrs.PlateCarree(), length=4, linewidth=1.1, barbcolor='white', flagcolor='red')
        ax.barbs(lons[::a_barbs,::a_barbs],lats[::a_barbs,::a_barbs],data_uwind[::a_barbs,::a_barbs], data_vwind[::a_barbs,::a_barbs], transform=ccrs.PlateCarree(), length=5,
             sizes=dict(emptybarb=0.25, spacing=0.4, height=0.5, barbcolor="white"),
             linewidth=0.5)

        manager = plt.get_current_fig_manager()
        manager.full_screen_toggle()
        return plt.gcf()
    
    def pre_click(self):
        if self.start_point > 1:
            self.start_point = self.start_point-1
            box = self.ids.box
            box.clear_widgets()
            box.add_widget(FigureCanvasKivyAgg(self.generate_map_image(self.start_point)))
        else:
            print('at last')

    def nxt_click(self):
        self.start_point = self.start_point+1
        box = self.ids.box
        box.clear_widgets()
        box.add_widget(FigureCanvasKivyAgg(self.generate_map_image(self.start_point)))

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.theme_platte = "BlueGray"
        Builder.load_file('plt.kv')
        return Matty()

MainApp().run() 

