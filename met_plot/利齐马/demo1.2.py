from pycwr.io.auto_io import radar_io 
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from pycwr.draw.RadarPlot import Graph, GraphMap
file = '/home/liyuan3970/Data/data/meto_data/radar_typhoon_liqima/wenzhou_rada/09/'
filename = r"Z_RADR_I_Z9577_20190809150400_O_DOR_SA_CAP.bin.bz2"
basedata = radar_io(file+filename) 
NRadar = basedata.ToPRD()

fig, ax = plt.subplots()
graph = GraphMap(NRadar, ccrs.PlateCarree())
graph.plot_vcs_map(ax, (121.0, 27.9), (121.7, 27.9), "dBZ", cmap="pyart_NWSRef")
ax.set_ylim([0,15])
ax.set_ylabel("Height (km)", fontsize=14)
ax.set_xlabel("Latitude, Longitude", fontsize=14)
ax.set_title("VCS exmaple", fontsize=16)
plt.show()