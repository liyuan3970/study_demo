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
fig, ax = plt.subplots(figsize=[15, 15])

graph = Graph(NRadar)
graph.plot_ppi(ax, 0, "dBZ", cmap="pyart_NWSRef")
graph.add_rings(ax, [0, 50, 100, 150, 200, 250, 300])
ax.set_title("example of PPI", fontsize=16)
ax.set_xlabel("Distance From Radar In East (km)", fontsize=14)
ax.set_ylabel("Distance From Radar In North (km)", fontsize=14)