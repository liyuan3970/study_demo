begin
;>---------------------------------------<
;            data　input
;>---------------------------------------<

;filetime = "gdas1.fnl0p25.2019081000.f00"

;time = "2019080806"
;time = "2019080912"
;time = "2019081000"
time = "2019081006"


;; time3 图片没有


wks = gsn_open_wks("png","test")
f = addfile("/home/liyuan3970/Data/data/meto_data/fnl/fnl_025/gdas1.fnl0p25."+time + ".f00.grib2", "r")

hgt = f->HGT_P0_L100_GLL0({50000}, :, :)
hgt = hgt * 0.1
u = f->UGRD_P0_L100_GLL0({20000}, ::4, ::4)
u = u * 2.5
v = f->VGRD_P0_L100_GLL0({20000}, ::4, ::4)
v =v * 2.5


rh = f->RH_P0_L100_GLL0({50000}, :, :)
t = f->TMP_P0_L100_GLL0({50000}, :, :)

ept=pot_temp_equiv(hgt, t, rh, -1, "rh") 
ept = ept-273.15
printVarSummary(ept)


;>---------------------------------------<
;            set for the wks and golbal res
;>---------------------------------------<
;wks = gsn_open_wks("eps","2019-08-10-06:00")
res = True
res@gsnDraw = False
res@gsnFrame = False
res@gsnLeftString = ""
res@gsnRightString = " "
;res@gsnCenterString = "2019-08-10-06"
;>---------------------------------------<
;            set for the map
;>---------------------------------------<
mpres = res
mpres@mpFillOn                = False
mpres@mpCenterLonF            = 120
mpres@mpMinLatF               = -10.
mpres@mpMaxLatF               = 55.
mpres@mpMinLonF               = 80.
mpres@mpMaxLonF               = 160.
mpres@mpDataBaseVersion       = "MediumRes"
mpres@mpDataSetName           = "Earth..4"
mpres@mpOutlineSpecifiers     = (/"China:states"/)
mpres@pmTickMarkDisplayMode  = "Always"
mpres@tmXBMajorLengthF = 0.005
mpres@mpOutlineOn =True
mpres@mpCountyLineThicknessF = 10
mpres@mpGeophysicalLineThicknessF = 0.01
mpres@mpPerimOn  =True
mpres@mpPerimLineThicknessF   = 0.8


;>---------------------------------------<
;>---------------------------------------<
;       set resource for contour plot
;>---------------------------------------<
cnres = res
cnres@cnSmoothingOn = True ;
cnres@cnSmoothingDistanceF   = 0.001
cnres@cnLevelSelectionMode   = "ManualLevels"
cnres@cnMinLevelValF = 60
cnres@cnMaxLevelValF = 80
cnres@cnLevelSpacingF = 2
cnres@cnInfoLabelOn = False
cnres@cnLineLabelsOn          =  True
cnres@cnLineLabelFontHeightF = 0.01
cnres@cnLineThicknessF = 2.2
cnres@cnLineLabelInterval = 1
cnres@cnLineColor = "red"
;>---------------------------------------<

mapplot = gsn_csm_map(wks, mpres)
cnplot = gsn_csm_contour(wks, ept, cnres)
overlay(mapplot, cnplot)
draw(mapplot)
frame(wks)
end