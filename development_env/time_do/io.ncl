begin
;>---------------------------------------<
;           读取数据
;>---------------------------------------<
ncol = 10
data = readAsciiTable("tpyrced_20061920.006", ncol, "float", 2)
one = ndtooned(data)
data_one = one(0:1038960)
data_latlon = reshape(one(0:1038960), (/1441,721/))
;数组的经纬度赋值
lon = fspan(0,180,1441)
lat = fspan(80,-10,721)
lon!0 = "lon"
lat!0 = "lat"
lon@long_name  = "lon"
lon@units      = "degrees-east"
lon&lon        = lon
lat@long_name  = "lat"
lat@units      = "degrees_north"
lat&lat        = lat
data_latlon!0 = "lon"
data_latlon!1 = "lat"
data_latlon&lon= lon
data_latlon&lat= lat
printVarSummary(data_latlon)

;截取浙江的经纬度内的数据，并输出成单唯数据
data_zj = data_latlon({lon|118:123},{lat|31:27})
data_zj_one = ndtooned(data_zj)
printVarSummary(data_zj)
data_lon = new((/41,33/), "float")
data_lat = new((/41,33/), "float")
do i=0,32
data_lon(:,i) = data_zj&lon
end do
do i=0,40
data_lat(i,:) = data_zj&lat
end do
data_one_lon = ndtooned(data_lon)
data_one_lat = ndtooned(data_lat)
printVarSummary(data_one_lon)
printVarSummary(data_one)
;>---------------------------------------<
;           插值成站点数据
;>---------------------------------------<
;;latlon 是站点的经纬度
lat_point=(/28.5,28.8,29.0/)
lon_point=(/118.2,120.2,121.5/)
; z1是站点数据
nnpntinit(data_one_lon,data_one_lat,data_zj_one)
z1 = nnpnt(lon_point,lat_point)
nnpntend()
printVarSummary(z1)
print("ok")
;>---------------------------------------<
;           线性关系
;>---------------------------------------<
a = 0.5
b = 0.3
z2 = a*z1+b
;>---------------------------------------<
;           插值成网格点
;>---------------------------------------<
;分辨率可能要调整 50 40
lon_net = fspan(118,123,50)
lat_net = fspan(31,27,40)
zi = natgrid(lon_point, lat_point, z2, lon_net, lat_net)

;>---------------------------------------<
;           输出成格点数据
;>---------------------------------------<

lon_net!0          = "lon_net"
lon_net@long_name  = "lon_net"
lon_net@units      = "degrees-east"
lon_net&lon        = lon_net
lat_net!0          = "lat_net"
lat_net@long_name  = "lat_net"
lat_net@units      = "degrees_north"
lat_net&lat        = lat_net
zi!0 = "lon_net"
zi!1 = "lat_net"
printVarSummary(zi)
f = addfile("test.nc", "c")
f->v = zi



end