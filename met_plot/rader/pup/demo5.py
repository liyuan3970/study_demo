import cinrad
#
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm, colors
from matplotlib import cm
import matplotlib
matplotlib.use('TkAgg')
# ncl调色板的配置
fid = open('radar.rgb')
data=fid.readlines()
n=len(data);
#print(n)
rgb=np.zeros((n,3))
for i in np.arange(n):
    #print(data[0].split(' '))
    rgb[i][0]=float(data[i].split(' ')[0])
    rgb[i][1]=data[i].split(' ')[1]
    rgb[i][2]=data[i].split(' ')[2]
print((rgb.shape))
#print(rgb[253])
cmaps= colors.ListedColormap(rgb)



#matplotlib.use('TkAgg')
f = cinrad.io.CinradReader('Z_RADR_I_Z9576_20190810000600_O_DOR_SA_CAP.bin.bz2')
tilt_number = 0
data_radius = 230
data_dtype = 'REF' # stands for reflectivity
ra = f.get_data(tilt_number, data_radius, data_dtype)

v = []
v.append(ra)
gmap =cinrad.easycalc.GridMapper(v)
grid = gmap(0.1)
lon = grid.lon
lat = grid.lat
data = grid.data

h = []
height = ra.height
rb = ra
rb.data = height
h.append(rb)
gcma = cinrad.easycalc.GridMapper(h)
gcmd = gcma(0.1)
lon2 = gcmd.lon
lat2 = gcmd.lat
hig = gcmd.data
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
# 创建3d图形的两种方式
# ax = Axes3D(fig)
ax = fig.add_subplot(111, projection='3d')
color_map =data.reshape(43*49)
print(color_map.shape)
# ax.scatter(lon2, lat2,hig,c=color_map,cmap=cmaps, s=5)

#ax.plot_surface(lon2, lat2,hig,facecolors=data,rstride=1, cstride=1, cmap=cmaps,shade=True)
ax.plot_surface(lon2, lat2,hig,facecolors=cmaps(data/100),rstride=1, cstride=1)
print(lon2.shape)
print(lat2.shape)
print(hig.shape)
print(data.shape)
# ax.scatter(lon2, lat2,hig,cmap='jet', s=40,
#              label='Points')
# ax.contourf(lon,lat,data,zdir='z',offset=-2)
ax.contourf(lon,lat,data,cmap=cmaps,zdir='z',offset=-20)


plt.show()