import matplotlib.pyplot as plt 
from mpl_toolkits.basemap import Basemap
 
plt.figure(figsize=(16,8))#定义图的大小
map1 = Basemap()#创建一个地图
map1.drawcoastlines()#绘制海岸线
map1.drawcountries(linewidth=1.5)#画上国家线
plt.show()#显示地图