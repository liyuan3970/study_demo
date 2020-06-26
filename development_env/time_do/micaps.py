from mdfs import Station
import matplotlib.pyplot as plt
import matplotlib.colors as ccolor
import matplotlib.cm as cmx
import cartopy.crs as ccrs
import cartopy.feature as cfeature

x = Station(r'tpyrced_20061920.006')
lon = x.data['Lon'] # 经度
lat = x.data['Lat'] # 纬度
var = x.data[603] # 气象要素

cm = plt.get_cmap('jet')
cNorm = ccolor.Normalize(vmin=min(var), vmax=max(var))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
c = scalarMap.to_rgba(var)
ax = plt.axes(projection=ccrs.PlateCarree())
ax.scatter(lon, lat, s=5, c=c)
ax.coastlines(resolution='10m')
ax.add_feature(cfeature.BORDERS)
plt.show()