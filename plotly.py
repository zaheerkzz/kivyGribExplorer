import numpy as np
import pandas as pd
import xarray as xr
import cartopy.crs as ccrs
from matplotlib import pyplot as plt

# path to file 
file_path = 'grb/ww3_wind_1.grb'
# load GRIB data into xarray
ds = xr.load_dataset(file_path, engine="cfgrib")
ds.sst[0].plot()
