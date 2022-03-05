# encoding=utf8
#!/usr/bin/python  
# -*- coding: utf-8 -*-  
import pymssql 
import pandas as pd
## 数据库部分
#-----------------------------------------------------------------------------------------------------------------------------------
## sqlserver
server = "172.21.158.201"    # 连接服务器地址
user = "down"# 连接帐号
password = "downx"# 连接密码
conn = pymssql.connect(server, user, password, "ZJSZDZDB")  #获取连接


## data
sql_location1 ="select lat,b.lon,b.IIiii,RR from TAB_Mws2019 as a left join TAB_StationInfo as b on a.IIiii=b.IIiii where\
(b.IIiii in (select IIiii from TAB_StationInfo where(City = '台州') and tTime between '2019-08-09 23:00' and '2019-08-10 06:00'))"

sql_location2 ="select lat,b.lon,b.IIiii,RR from TAB_Aws2019 as a left join TAB_StationInfo as b on a.IIiii=b.IIiii where\
(b.IIiii in (select IIiii from TAB_StationInfo where(City = '台州') and tTime between '2019-08-09 23:00' and '2019-08-10 06:00'))"


df_location1 = pd.read_sql(sql_location1 , con=conn)
df_location2 = pd.read_sql(sql_location2 , con=conn)
station_all = pd.concat([df_location1,df_location2])
grouped = station_all.groupby('IIiii')

# 存储最大降水的数据
data = {"name":[],"lat":[],"lon":[],"RMax":[]}
for i in grouped.size().index:
    data['name'].append(grouped.get_group(i)['IIiii'].iloc[0])
    data['lat'].append(grouped.get_group(i)['lat'].iloc[0])
    data['lon'].append(grouped.get_group(i)['lon'].iloc[0])
    data['RMax'].append(grouped.get_group(i)['RR'].max())

import pandas as pd
from scipy.interpolate import griddata
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from math import ceil, floor


import numpy as np

import xarray as xr

import pandas as pd

import os

#-----------------------------------------------------------------------------------------------------------------------------------
lat = data['lat']
lon = data['lon']
RR = data['RMax']
Zi = RR
x = np.arange(120.0,122.0,0.05)
#print(x)
y = np.arange(27.8,29.5,0.05)
nx0 =len(x)
ny0 =len(y)
X, Y = np.meshgrid(x, y)#100*100

P = np.array([X.flatten(), Y.flatten() ]).transpose()
    
Pi =  np.array([lon, lat ]).transpose()

Z_linear = griddata(Pi, Zi, P, method = "cubic").reshape([ny0,nx0])



from mpl_toolkits.basemap import Basemap
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
#from osgeo import gdal
import numpy as np
import cartopy.crs as ccrs
import shapefile
import matplotlib as mpl
import xarray as xr
from matplotlib.font_manager import FontProperties
import netCDF4 as nc
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

import matplotlib

plt.rcParams.update({'font.size': 20})
fig = plt.figure(figsize=[12,18]) 
ax = fig.add_subplot(111)


def basemask(cs, ax, map, shpfile):

    sf = shapefile.Reader(shpfile)
    vertices = []
    codes = []
    for shape_rec in sf.shapeRecords():
        if shape_rec.record[0] >= 0:  
            pts = shape_rec.shape.points
            prt = list(shape_rec.shape.parts) + [len(pts)]
            for i in range(len(prt) - 1):
                for j in range(prt[i], prt[i+1]):
                    vertices.append(map(pts[j][0], pts[j][1]))
                codes += [Path.MOVETO]
                codes += [Path.LINETO] * (prt[i+1] - prt[i] -2)
                codes += [Path.CLOSEPOLY]
            clip = Path(vertices, codes)
            clip = PathPatch(clip, transform = ax.transData)    
    for contour in cs.collections:
        contour.set_clip_path(clip)    



def makedegreelabel(degreelist):
    labels=[str(x)+u'°E' for x in degreelist]
    return labels

print(Z_linear.shape,x.shape)
data_xr = xr.DataArray(Z_linear, coords=[ y,x], 
                    dims=["lat", "lon"])


m = Basemap(llcrnrlon=120.0,
    llcrnrlat=27.8,
    urcrnrlon=122,
    urcrnrlat=29.5,
    resolution = None, 
    projection = 'cyl')

cs = data_xr.plot.contourf(ax=ax, cmap='Spectral_r')

filepath = "/home/liyuan3970/study_demo/met_plot/Basemap/"
m.readshapefile(filepath+'taizhou','taizhou',color='k',linewidth=1.2)
basemask(cs, ax, m, filepath+'taizhou') 
parallels = np.arange(27.8,29.5,0.05)
# labels = [left,right,top,bottom]
m.drawparallels(parallels,labels=[True,True,True,True],color='dimgrey',dashes=[2, 3],fontsize= 14)  # ha= 'right'
meridians = np.arange(120.0,122.0,0.05)
m.drawmeridians(meridians,labels=[True,True,False,True],color='dimgrey',dashes=[2, 3],fontsize= 14)
plt.rcParams.update({'font.size':25})
plt.show()
