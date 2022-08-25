import xarray as xr
import cartopy.crs as ccrs
from matplotlib import pyplot as plt
import pygrib


# path to file 
file_path = file_path = 'grb/dd/gfs1deg_12hr_wind_6.grb'
# load GRIB data into xarray
# ds = xr.load_dataset(file_path, engine="cfgrib")
grbs = pygrib.open(file_path)
for grb in grbs:
    print(grbs)
# print(ds.sst[0])
# ds.rsn[0].att

# plt.figure(figsize=(14, 6))
# ax = plt.axes(projection=ccrs.PlateCarree())
# ax.set_global()
# ds.sst[0].plot.pcolormesh(
#     ax=ax, transform=ccrs.PlateCarree(), x=None, y=None, add_colorbar=False
# )
# ax.coastlines()
# ax.set_ylim([0, 90])
plt.savefig("test.png")