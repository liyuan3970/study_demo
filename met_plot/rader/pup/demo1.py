import cinrad
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
f = cinrad.io.CinradReader('Z_RADR_I_Z9576_20190810000600_O_DOR_SA_CAP.bin.bz2')
tilt_number = 0
data_radius = 230
data_dtype = 'REF' # stands for reflectivity
ra = f.get_data(tilt_number, data_radius, data_dtype)
print('height',ra.height.shape)
height = ra.height
print(height.shape)
data = ra.data
values = data
print(values.shape)
azimuths = np.radians(np.linspace(0, 360, 366))
zeniths = np.arange(0, 230, 1)
print(azimuths.shape)
print(zeniths.shape)
r, theta = np.meshgrid(zeniths, azimuths)
print(r.shape)
print(theta.shape)
#fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
# 创建3d图形的两种方式
# ax = Axes3D(fig)
ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(r, theta, data, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
ax.contourf(r, theta,data,zdir='z',offset=-2)
# zdir : 'z' | 'x' | 'y' 表示把等高线图投射到哪个面
# offset : 表示等高线图投射到指定页面的某个刻度
# ax.contourf(r, theta, height,zdir='z',offset=-2)
# 设置图像z轴的显示范围，x、y轴设置方式相同
# ax.set_zlim(-2,2)

plt.show()