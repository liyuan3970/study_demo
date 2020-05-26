begin
filename = "/home/liyuan3970/Data/data/meto_data/fnl/fnl_025/gdas1.fnl0p25.2019080918.f00"
f = addfile(filename + ".grib2", "r")
hgt = f->HGT_P0_L100_GLL0({50000}, :, :)
hgt = hgt * 0.1
u = f->UGRD_P0_L100_GLL0({85000}, ::4, ::4)
u = u * 2.5
v = f->VGRD_P0_L100_GLL0({85000}, ::4, ::4)
v =v * 2.5
wks = gsn_open_wks("x11", filename)
res = True
res@gsnDraw = False
res@gsnFrame = False
res@gsnLeftString = ""
res@gsnRightString = ""
;>---------------------------------------<
;            set for the map
;>---------------------------------------<
mpres = res
mpres@mpFillOn                = False
mpres@mpMinLatF               = -10.
mpres@mpMaxLatF               = 55.
mpres@mpMinLonF               = 80.
mpres@mpMaxLonF               = 160.
mpres@mpDataBaseVersion       = "MediumRes"
mpres@mpDataSetName           = "Earth..4"
mpres@mpOutlineSpecifiers     = (/"China:states"/)
mpres@pmTickMarkDisplayMode  = "Always"
mpres@tmXBMajorLengthF = 0.005
;>---------------------------------------<
;>---------------------------------------<
;       set resource for contour plot
;>---------------------------------------<
cnres = res
cnres@cnSmoothingOn = True ;
cnres@cnSmoothingDistanceF   = 0.001
cnres@cnLevelSelectionMode   = "ManualLevels"
cnres@cnMinLevelValF = 500
cnres@cnMaxLevelValF = 600
cnres@cnLevelSpacingF = 4
cnres@cnInfoLabelOn = False
cnres@cnLineLabelsOn          =  True
cnres@cnLineLabelFontHeightF = 0.01
cnres@cnLineThicknessF = 5.0
cnres@cnLineLabelInterval = 1
;>---------------------------------------<
;>---------------------------------------<
;     set resource for windBarb plot
;>---------------------------------------<
vcres                           = res
vcres@gsnAddCyclic = False
vcres@vcGlyphStyle               = "WindBarb"
vcres@vcRefLengthF               = 0.02
vcres@vcRefAnnoOn               = False
vcres@vcWindBarbLineThicknessF  = 2
vcres@vcWindBarbColor = "blue"
vcres@vcMinMagnitudeF = 2
vcres@vcWindBarbTickLengthF = 0.35
vcres@vcMinDistanceF            =0.02
;>---------------------------------------<
mapplot = gsn_csm_map(wks, mpres)
cnplot = gsn_csm_contour(wks, hgt, cnres)
vcplot = gsn_csm_vector(wks, u, v, vcres)
overlay(mapplot, cnplot)
overlay(mapplot, vcplot)
draw(mapplot)
frame(wks)
end