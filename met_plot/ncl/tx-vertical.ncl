begin
;>---------------------------------------<
;            data　input
;>---------------------------------------<
filename = "gdas1.fnl0p25.2019081006.f00"
f = addfile(filename + ".grib2", "r")
vwnd1 = f->VGRD_P0_L100_GLL0
uwnd1 = f->UGRD_P0_L100_GLL0
omega1 = f->VVEL_P0_L100_GLL0


u=uwnd1(10:30,:,:)
v=vwnd1(10:30,:,:)
w=omega1
u1 = u({lv_ISBL5|:},{lat_0|30},{lon_0|100:160})  ;lat0.25 * lon0.25   ---->25N127.5E
v1 = v({lv_ISBL5|:},{lat_0|30},{lon_0|100:160})
w1 = w({lv_ISBL9|:},{lat_0|30},{lon_0|100:160})
w1 = w1 *100
print(max(w1))
print(min(w1))
printVarSummary(v1)
printVarSummary(w1)
;print(lat({lat_0|50})
wks  = gsn_open_wks("eps","x-vertical")
   ;gsn_define_colormap(wks,"gui_default")

   res                  = True  
   res@cnLinesOn        = False
   res@cnLineLabelsOn   = False
   res@cnInfoLabelOn    = False
   res@tmXTOn           = False   ; and right tickmarks.
   res@tmYROn           = False
   ;res@vcRefMagnitudeF  = 0.0001                
   res@vcRefAnnoString1On = True
   res@vcRefAnnoString1   = "5m/s"
   res@vcRefAnnoOrthogonalPosF   = -1.095  
   res@vcRefAnnoString2On = False     
   res@vcRefLengthF     = 0.8               
   res@vcGlyphStyle     = "LineArrow"
   ;res@vcMinDistanceF   = 0.008
   res@vcMapDirection   = False

   res@vpWidthF         = 0.75
   res@vpHeightF        = 0.6
   res@tiMainFontHeightF = 0.02
   res@gsnLeftString   = ""
   res@gsnRightString  = ""            
   res@tiYAxisString   = "666666"
   ;res@tmYRMode        = "Automatic"

   ;res@tmXBMode   = "Explicit"


vcres=True
  vcres@vcLineArrowColor        = "purple"        ; change vector color
  ;vcres@vcLineArrowThicknessF   = 2.0               ; change vector thickness
  vcres@vcRefAnnoOn  =False
  vcres@vcRefAnnoArrowUseVecColor    =False ;Ref颜色独立
  vcres@vcRefAnnoPerimOn =False
  vcres@vcRefAnnoArrowLineColor="purple"
  vcres@vcRefAnnoString1              ="2m/s" ;Ref框里写字
  vcres@vcRefAnnoFontHeightF  =0.02
  vcres@vcRefAnnoFontThicknessF =0.02
  vcres@vcRefAnnoJust    =      "TopRight"

  vcres@vcRefAnnoString2   =" "           ;去掉reference vector字样
  ;vcres@vcRefMagnitudeF           = 2            ; define vector ref mag
  vcres@vcRefLengthF              = 0.3          ; define length of vec ref
  vcres@vcRefAnnoOrthogonalPosF   =-1.36 ;;;-1.36            ; move ref vector
  vcres@vcMinDistanceF            =0.02
  vcres@vcLineArrowThicknessF =1.5

  vcres@vcVectorDrawOrder       = "PostDraw"        ; draw vectors last



  ;------------------------------------------------------
  ;
  ;
  ;------------------------------------------------------
vcres@cnFillOn = True
;vcres@cnLinesOn = False
;vcres@cnLineLabelsOn = False
;vcres@cnInfoLabelOn = False
;vcres@lbLabelBarOn = True;False
  
vcres@cnLevelSelectionMode="ManualLevels"
vcres@cnMinLevelValF=-25
vcres@cnMaxLevelValF=25
vcres@cnLevelSpacingF=5
vcres@cnFillColors = (/34,54,74,84,98,114,132,148,162,178,215,225/)
vcres@tiYAxisString   = " "
vcres@gsnLeftString   = "Vertical Wind";
vcres@gsnRightString = " "

   plot = gsn_csm_pres_hgt_vector(wks,v1,u1,w1,vcres)   
  ; plot = gsn_csm_vector(wks,u1, w1,vcres)
end     
 














