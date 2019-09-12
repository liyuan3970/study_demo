begin
filename = "gdas1.fnl0p25.2019080406.f00"
f = addfile(filename + ".grib2", "r")

; fnl数据计算水汽通量
rh = f->RH_P0_L100_GLL0({85000}, :, :)

t = f->TMP_P0_L100_GLL0({85000}, :, :)

u = f->UGRD_P0_L100_GLL0({85000}, :, :)

v = f->VGRD_P0_L100_GLL0({85000}, :, :)

p =850

printVarSummary(rh)

printVarSummary(t)

printVarSummary(u)

printVarSummary(v)

;计算水汽通亮
q1 = mixhum_ptrh(conform(rh,p,0),t,rh,2)
copy_VarCoords(rh, q1)
printVarSummary(q1)

;计算水汽通量
qu1 = q1 * u
qv1 = q1 * v

copy_VarCoords(rh, qu1)
copy_VarCoords(rh, qv1)

printVarSummary(qu1)
printVarSummary(qv1)

;计算水汽通量散度
qduv = uv2dvF_Wrap(qu1,qv1)

printVarSummary(qduv)
end

























