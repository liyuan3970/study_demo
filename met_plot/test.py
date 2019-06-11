
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.pyplot as plt

# 数据读取及时间平均处理
ds = xr.open_dataset('EC-Interim_monthly_2018.nc')
temp = (ds['t2m'] - 273.15).mean(dim='time')  #把温度转换为℃并对其时间纬求平均
temp.attrs['units'] = 'deg C'  #温度单位转换为℃
# 创建画图空间


proj = ccrs.PlateCarree()  #创建投影

fig = plt.figure(figsize=(9,6))  #创建页面
print('ok')
ax = fig.subplots(1, 1, subplot_kw={'projection': proj})  #子图
# 设置地图属性:加载国界、海岸线、河流、湖泊

ax.add_feature(cfeat.BORDERS.with_scale('50m'), linewidth=0.8, zorder=1)
ax.add_feature(cfeat.COASTLINE.with_scale('50m'), linewidth=0.6, zorder=1)  
ax.add_feature(cfeat.RIVERS.with_scale('50m'), zorder=1)  
ax.add_feature(cfeat.LAKES.with_scale('50m'), zorder=1)  
# 设置网格点属性

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, 
  linewidth=1.2, color='k', alpha=0.5, linestyle='--')
gl.xlabels_top = False  #关闭顶端标签
gl.ylabels_right = False  #关闭右侧标签
gl.xformatter = LONGITUDE_FORMATTER  #x轴设为经度格式
gl.yformatter = LATITUDE_FORMATTER  #y轴设为纬度格式
# 设置colorbar
cbar_kwargs = {
   'orientation': 'horizontal',
   'label': '2m temperature (℃)',
   'shrink': 0.8,
   'ticks': np.arange(-30,30+5,5)
}
# 画图

levels = np.arange(-30,30+1,1)
temp.plot.contourf(ax=ax, levels=levels, cmap='Spectral_r', 
    cbar_kwargs=cbar_kwargs, transform=ccrs.PlateCarree())
fig.show()
print('ok')