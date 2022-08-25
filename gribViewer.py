import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import pygrib
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cfgrib

class GRIBViewer:
    def __init__(self):

        # path to file 
        file_path = 'grb/ww3_wind_1.grb'

        # open file using pygrib
        self.grbs = pygrib.open(file_path)
        # load GRIB data into xarray
        self.ds = xr.load_dataset(file_path, engine="cfgrib")

    # prints GRIB data segment to terminal 
    def display_grib_results(self):
        # GRIB data segments
        print("GRIB data segments:")
        # print(self.ds.sst[0].GRIB_latitudeOfFirstGridPointInDegrees)
        print(self.ds.sst)
        # print(self.ds.sst[2])

    # prints each segment item values
    def display_grib_value(self):
        # print all GRIB values for each item
        print("GRIB values Time Intervals:")
        print(self.grbs.message(3))
        for grb in self.grbs:
            # print(grb.keys())
            print(grb)
            print(grb.temp)
        #     print(grb.latitudeOfFirstGridPointInDegrees)
        #     print(grb.longitudeOfFirstGridPointInDegrees)
        #     print(grb.latitudeOfLastGridPointInDegrees)
        #     print(grb.longitudeOfLastGridPointInDegrees)

    # generate MAP image for each time interval
    def generate_map_image(self):
        # draw map from GRIB data
        for count, grb in enumerate(self.grbs):
            lats, lons = grb.latlons()

            # wind direction
            grb_uwind = grb #U 10m wind component for 2012-03-26 @00UTC
            grb_vwind = grb #V 10m wind component for 2012-03-26 @00UTC
            data_uwind = grb_uwind.values #U 10m wind values in m/s
            data_vwind = grb_vwind.values #V 10m wind values in m/s

            map_crs = ccrs.LambertConformal(central_longitude=-100, 
                                            central_latitude=35,
                                            standard_parallels=(30, 60))

            data_crs = ccrs.PlateCarree()
            fig = plt.figure(1, figsize=(16, 12))
            ax = plt.subplot(1, 1, 1, projection=map_crs)

            # x1= grb.latitudeOfFirstGridPointInDegrees
            # y1=grb.longitudeOfFirstGridPointInDegrees
            # x2=grb.latitudeOfLastGridPointInDegrees
            # y2=grb.longitudeOfLastGridPointInDegrees

            ax.set_extent([-130, -72, 20, 55], data_crs)

            # ax.add_feature(cfeature.COASTLINE.with_scale("50m"))
            # DRAW MAP
            # Create a feature for States/Admin 1 regions at 1:50m from Natural Earth
            # states_provinces = cfeature.NaturalEarthFeature(
            #     category='cultural',
            #     name='admin_1_states_provinces_lines',
            #     scale='50m',
            #     facecolor='none')

            ax.add_feature(cfeature.LAND)
            ax.add_feature(cfeature.COASTLINE)
            ax.add_feature(cfeature.OCEAN)
            ax.add_feature(cfeature.LAKES)
            # ax.add_feature(states_provinces, edgecolor='gray')
            ax.add_feature(cfeature.STATES, edgecolor='gray')

            # ax.gridlines()
            # ax.add_feature(cfeature.STATES.with_scale('50m'))

            # temp data 
            # x = grb.latitudeOfFirstGridPointInDegrees
            # y = grb.latitudeOfLastGridPointInDegrees
            
            cntr = ax.contourf(lons, lats, grb.values, transform=data_crs)
            # plt.colorbar(cntr, orientation='vertical')
            plt.colorbar(cntr, location='right', label='', shrink=0.9)
            plt.title(f"Forcast Time: {grb}")

            # plot wind direction on graph
            ax.barbs(lons[::6,::6],lats[::6,::6],data_uwind[::6,::6], data_vwind[::6,::6], transform=ccrs.PlateCarree(), length=5, linewidth=1.4, barbcolor='silver', flagcolor='yellow')

            # plt.savefig(f"ww3_wind_img/ww3_wind{count+1}.png")
            plt.show()

if __name__ == '__main__':
    gv = GRIBViewer()
    # gv.display_grib_results()
    # gv.display_grib_value()
    gv.generate_map_image()