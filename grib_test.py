import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy
import cartopy.feature as cfeature

file_path = 'grb/dd/gfs1deg_wind_7.grb'

ds = xr.load_dataset(file_path, engine="cfgrib")
print(ds.sst[0])
# ds = ds - 273.15
# print('\n\n\n')
# print(ds.rsn[0])
# sst, rsn
ds.rsn[0].plot(cmap=plt.cm.coolwarm)
fig = plt.figure(figsize=(30, 20))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAKES, alpha=1)
ax.add_feature(cfeature.RIVERS)
plot = ds.rsn[0].plot(
    cmap=plt.cm.coolwarm, transform=ccrs.PlateCarree(), cbar_kwargs={"shrink": 0.6}
)
plt.title("ERA5 - 2m temperature British Isles March 2019")

plt.savefig("ssss1.png")

