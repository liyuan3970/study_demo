import netCDF4 as nc
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
obj=nc.Dataset('I:\\Learn\\Python_related\\850hPa_uv_global_1mon_4daily.nc')
u=obj.variables['u'][0,35:76,70:141]
v=obj.variables['v'][0,35:76,70:141]
lat=obj.variables['latitude'][:];lon=obj.variables['longitude'][:]
m=Basemap(projection='cyl',llcrnrlat=15,urcrnrlat=55,llcrnrlon=70,urcrnrlon=140,resolution='l')
lons,lats=m.makegrid(71,41)
lats=lats[::-1]
x,y=m(lons,lats)
m.drawparallels(np.arange(15.,56.,10.),labels=[1,0,0,0],fontsize=15)
m.drawmeridians(np.arange(75.,141.,15.),labels=[0,0,0,1],fontsize=15)
m.readshapefile('E:\\shp_map\\bou2_4p','bou2_4p.shp',linewidth=1,drawbounds=True,color='gray')
m.drawlsmask()
curve=m.contour(lons,lats,u,colors='k')
shade=m.contourf(lons,lats,u)
m.colorbar(shade)
plt.clabel(curve,fmt='%1.0f')
# print help(plt.quiver)
# wind=m.quiver(lons,lats,u,v,width=0.002,headwidth=2,headlength=4)
plt.title('shaded plot',size=20)
plt.show()
