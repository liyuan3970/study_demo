from __future__ import print_function
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from copy import deepcopy
import multidop
import pyart
import tempfile
import os
import glob
import time


from pycwr.io.auto_io import radar_io 
import numpy as np
import pandas as pd
import xarray as xr
import pyart
grad_data = pyart.io.read_grid('/home/liyuan3970/Data/data/meto_data/radar_typhoon_liqima/grid.nc')
display = pyart.graph.GridMapDisplay(grad_data)
fig = plt.figure(figsize=[15, 7])

# panel sizes
map_panel_axes = [0.05, 0.05, .4, .80]
level = 0
vmin = -8
vmax = 64
# panel 1, basemap, radar reflectivity and NARR overlay
ax1 = fig.add_axes(map_panel_axes)
#display.plot_basemap(lon_lines = np.arange(-104, -93, 2) )
x, z, data = display.plot_latlon_slice("reflectivity", coord1=(120.2, 28.0), coord2=(121.1, 28.0),vmin=-10,vmax=10)
#x, z, data = display.plot_latlon_slice("w", coord1=(121.2, 28.5), coord2=(121.1, 28.0),vmin=0,vmax=70)
#print(data.shape)
print(data.shape)
def onclick(event):
    print("*****")
    print(data[int(event.xdata),int(event.ydata)])
    print('%s click:  x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', 
           event.x, event.y, event.xdata, event.ydata))
#cid = fig.canvas.mpl_connect('button_press_event', onclick)
cid = fig.canvas.mpl_connect('motion_notify_event', onclick)
plt.show()