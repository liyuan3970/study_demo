import cinrad
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from cinrad.visualize import PPI
import matplotlib
matplotlib.use('TkAgg')
f = cinrad.io.CinradReader('Z_RADR_I_Z9576_20190810000600_O_DOR_SA_CAP.bin.bz2')
tilt_number = 0
data_radius = 230
data_dtype = 'REF' # stands for reflectivity
r = f.get_data(tilt_number, data_radius, data_dtype)
height = r.height
r.data = height
v = []
v.append(r)
f =cinrad.easycalc.GridMapper(v)
grid = f(0.1)
lon = grid.lon
print(lon.shape)
lat = grid.lat
print(grid.data)
print(type(f))
# PPI(grid)
data = grid.data

f1 = cinrad.io.CinradReader('Z_RADR_I_Z9576_20190810000600_O_DOR_SA_CAP.bin.bz2')
r1 = f1.get_data(tilt_number, data_radius, data_dtype)
v1 = []
v1.append(r)
f2 =cinrad.easycalc.GridMapper(v1)
grid1 = f2(0.1)
data1 = grid1.data

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
# 创建3d图形的两种方式
ax = Axes3D(fig)
# ax.scatter(lon, lat,data,cmap='jet', s=40,
#              label='Points')
ax.contourf(lon,lat,data1,zdir='z',offset=-2)
plt.show()