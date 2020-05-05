begin 
filename = "Z_RADR_I_Z9577_20190809193400_O_DOR_SA_CAP.bin.bz2.nc"

lat0 = 27.8
lat1 = 28.4

lon0 = 121.1
lon1 = 121.9
f = addfile(filename,"r")
u = f->u(0,:,:,:)
v = f->v(0,:,:,:)
w = f->w(0,:,:,:)
lat = f->lat
lon = f->lon
vr = uv2vr_cfd (u,v,lat,lon, 0) 
vr = vr*1000
copy_VarCoords(u, vr)
wind = sqrt(u*u+v*v)
copy_VarCoords(u, wind)



area = wind({heigh|0.0:2333.33},{lat|lat0:lat1},{lon|lon0:lon1})
printVarSummary(area)

wnd = w({heigh|0.0:2333.33},{lat|lat0:lat1},{lon|lon0:lon1})
area@_FillValue = -9.969209968386869e+36
wnd@_FillValue = -9.969209968386869e+36
area =where(area(:,:,:).lt.1.409859194343776e+37,area,area@_FillValue)
wnd =where(wnd(:,:,:).lt.9.969209968386869e+36,wnd,0)


ave_vr = vr({heigh|0.0:2333.33},{lat|lat0:lat1},{lon|lon0:lon1})
print("ave_vr:  "+avg(ave_vr))
print("max_vr:  "+max(ave_vr))
print("area_max:  "+max(area))
print("wnd_max:  "+max(wnd))
print("area_avg:  "+avg(area))

;print(ave_vr)






end