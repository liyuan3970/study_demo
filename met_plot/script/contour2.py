from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

meteo_file = "'EC-Interim_monthly_2018.nc'"
fh = Dataset('EC-Interim_monthly_2018.nc')#(meteo_file, mode='r')

# 获取每个变量的值
lons = fh.variables['longitude'][:]
lats = fh.variables['latitude'][:]
tlml = fh.variables['t2m'][:]

tlml_units = fh.variables['t2m'].units


# 经纬度平均值
lon_0 = lons.mean()
lat_0 = lats.mean()

m = Basemap(lat_0=lat_0, lon_0=lon_0)
lon, lat = np.meshgrid(lons, lats)
xi, yi = m(lon, lat)

# Plot Data
# 这里我的tlml数据是24小时的，我这里只绘制第1小时的（tlml_0）
tlml_0 = tlml[0:1:, ::, ::]
cs = m.pcolor(xi, yi, np.squeeze(tlml_0))

# Add Grid Lines
# 绘制经纬线
m.drawparallels(np.arange(-90., 91., 20.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 40.), labels=[0,0,0,1], fontsize=10)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(tlml_units)

# Add Title
plt.title('Surface Air Temperature')
plt.show()

fh.close()