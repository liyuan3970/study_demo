from __future__ import print_function
import numpy as np
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

f1 = r"src/Z_RADR_I_Z9577_20190809162900_O_DOR_SA_CAP.bin.bz2"

basedata1 = radar_io(f1)
radar = basedata1.ToPyartRadar()
fig = plt.figure(figsize=[8, 8])
display = pyart.graph.RadarDisplay(radar)
display.plot('reflectivity', sweep=0)
display.set_limits((-300, 300), (-300, 300))



data = radar.fields['reflectivity']['data']
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