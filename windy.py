import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import pygrib
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cfgrib
import kivy

class GRIBViewer:
    def __init__(self):

        # path to file 
        file_path = 'grb/dd/gfs_wind_7.grb'

        # open file using pygrib
        self.grbs = pygrib.open(file_path)
        # load GRIB data into xarray
        self.ds = xr.load_dataset(file_path, engine="cfgrib")

    # prints GRIB data segment to terminal 
    def display_grib_results(self):
        # GRIB data segments
        print("GRIB Data Segments:")
        print(self.ds.vp)

    # prints each segment item values
    def display_grib_value(self):
        print("GRIB Data Values:")
        # print all GRIB values for each item
        for grb in self.grbs:
            print(grb)

    # generate MAP image for each time interval
    def generate_map_image(self):
        # draw map from GRIB data
        for count, grb in enumerate(self.grbs):
            lats, lons = grb.latlons() 
            map_crs = ccrs.LambertConformal(central_longitude=-100, 
                                            central_latitude=35,
                                            standard_parallels=(30, 60))

            data_crs = ccrs.PlateCarree()
            fig = plt.figure(1, figsize=(16, 12))
            ax = plt.subplot(1, 1, 1, projection=map_crs)
            ax.set_extent([-130, -72, 20, 55], data_crs)

            ax.add_feature(cfeature.COASTLINE.with_scale("50m"))
            # ax.add_feature(cfeature.STATES.with_scale('50m'))

            # add temp bar
            # plot = self.ds.vp[0].plot(transform=ccrs.PlateCarree(), cbar_kwargs={"shrink": 0.6})
            # add title to chart
            plt.title(f"Forcast Time: {grb}")

            ax.contourf(lons, lats, grb.values, transform=data_crs)
            plt.savefig(f"surfpres_image/oceans{count+1}.png")
            # plt.show()

if __name__ == '__main__':
    gv = GRIBViewer()
    gv.generate_map_image()