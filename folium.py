# libraries import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from folium.plugins import plugins


# return label
file_path = 'grb/ww3_wind_1.grb'

ds = xr.load_dataset(file_path, engine="cfgrib")
print(ds.sst[0])
# # Saving lat e lon and removing NaN
# points = (ds.sst[0].latitude.fillna(0),df.longitude.fillna(0))
# coordinates =[]
# # Setting lat and long 
# lat = points[0]
# long = points[1]
# # Latitude and longitude that will open map. Here I put central of city São Paulo
# mapa = folium.Map(location=[-23.5489, -46.6388])
# # Append latitude and longitude coordinates array
# for la,lo in zip(lat,long):
#     coordinates.append([la,lo])
   
# # We have about 700000 lines, but jupyter notebook ins't possible to show all these points.
# # To impress all data you can salve as a html file 
# #mapa.save("map.html")
# # Or to show onlye a piece
# mapa.add_child(plugins.HeatMap(coordinates[0:40000]))
