begin
f=addfile("china-hwfmonth.nc", "r")
;dd=filwgts_lanczos(3, 1, 0.125, -999., 1)
ap=f->ap
printVarSummary(ap)

;print(b(:,:,:))


time=ispan(0,63,1)
year=ispan(1951,2014, 1)
a=dim_sum_n(ap,1)
c=dtrend_msg_n(year,a(1:64,:,:), True, True, 0)
copy_VarCoords(ap(:,0,:,:), c)
b=c
copy_VarCoords(ap(0,0,:,:), b(0,:,:))
b!0="time"
b&time=time

b&time@lon_name="year"
b&time@units="year"
w=sqrt(cos(0.01745329*b&lat))
wp=b*conform(b,w,1)
copy_VarCoords(b, wp)
printVarSummary(wp)
optEOF = False
optETS = False       
neval  =2
eof= eofunc_Wrap(wp({lat|15:55},{lon|70:140},{time|:}),neval,optEOF)
eof_ts=eofunc_ts_Wrap (wp({lat|15:55},{lon|70:140},{time|:}),eof, optETS)
eof_ts(0,:)=-eof_ts(0,:)/100
eof(0,:,:)=-100*eof(0,:,:)
eof_ts(1,:)=-eof_ts(1,:)/100
eof(1,:,:)=-100*eof(1,:,:)
f1=addfile("hwfts.nc", "c")
f1->ts=eof_ts
f2=addfile("hwfe.nc", "c")
f2->e=eof
wks = gsn_open_wks("png","1951_2014hwf_EOF—---test")

res=True
res@gsnDraw = False
res@gsnFrame = False
res@gsnAddCyclic        = False
res@mpCenterLonF         = 100  
res@mpLimitMode       = "LatLon"
res@mpMinLatF         = 15         
res@mpMaxLatF         = 55
res@mpMinLonF         = 70
res@mpMaxLonF         = 140
res@cnFillOn       = True
;res@cnFillPattern ="Explicit"

res@mpFillOn              = True     ; turn on color fill
res@mpDataSetName         = "Earth..4"
res@mpDataBaseVersion     = "MediumRes"
;res@mpAreaMaskingOn       = True
res@mpMaskAreaSpecifiers  = (/"China","taiwan"/)
res@mpOutlineSpecifiers   = (/"China"/)

res@mpLandFillColor            = "white"
res@mpInlandWaterFillColor     = "white"
res@mpOceanFillColor           = "white"
res@mpFillBoundarySets         = "NoBoundaries"
res@mpOutlineBoundarySets      = "NoBoundaries"
res@mpNationalLineColor        = "black"
res@mpProvincialLineColor      = "black"
res@mpGeophysicalLineColor     = "black"
res@mpNationalLineThicknessF   = 2
res@mpProvincialLineThicknessF = 1

res@lbBoxLinesOn          =False

res@cnFillOn              = True
res@cnFillDrawOrder       = "PreDraw"
res@cnLineLabelsOn        = False
res@cnLinesOn             = True    ; turn of contour lines
res@cnLineDrawOrder       = "PreDraw"
;res@cnLevelSpacingF       = 0.5      ; contour spacing
;res@lbLabelAutoStride          = True
res@lbLabelBarOn = False
res@pmTickMarkDisplayMode = "Always"
res@cnSmoothingOn      =True
res@cnSmoothingDistanceF = 0.01
res@cnSmoothingTensionF = -1.5
res@cnRasterSmoothingOn= True

res@tmXBMode = "Explicit"
res@tmXBValues = (/"70","80","90","100","110","120","130","140"/)
res@tmXBLabels  = (/"70E","80E", "90E", "100E","110E","120E","130E","140E"/)

res@cnMissingValFillColor="white"
res@vpXF = 0     ;左边距
res@vpYF = 0.95      ;上边距
res@vpWidthF  = 0.8              ; height and width of plot
res@vpHeightF = 0.8
res@tmXBLabelFontHeightF  = 0.02
res@tmYLLabelFontHeightF  = 0.02
res@cnLevelSelectionMode="ManualLevels"
res@cnMinLevelValF=-4
res@cnMaxLevelValF=12
res@cnLevelSpacingF=2
res@cnFillColors=(/18,50,114,129,145,161,177,193,200,215,240/)



rts           = True
rts@gsnDraw = False
rts@gsnFrame = False
rts@vpHeightF = 0.40        ; Changes the aspect ratio
rts@vpWidthF  = 0.80
rts@vpXF      = 0.80        ; change start locations
rts@vpYF      = 0.75        ; the plot
rts@tiYAxisString = ""                  
rts@tiXAxisString = "year"
rtsP                      = True            ; modify the panel plot
rtsP@gsnMaximize          = True            ; large format
;rts@trYMaxF=1.3
;rts@trYMinF=-1.8
  
rts@gsnYRefLine           = 0.              ; reference line   
rts@gsnXYBarChart         = True            ; create bar chart 
rts@gsnAboveYRefLineColor = "red"           ; above ref line fill red
rts@gsnBelowYRefLineColor = "blue"          ; below ref line fill blue
 ;rts@tmYMajorGrid          = True
 ;rts@tmYMajorGridLineColor = "black"
 ;rts@tmYMajorGridThicknessF=0.3
 ;rts@tmXMajorGrid          = True
 ;rts@tmXMajorGridLineColor = "black"
 ;rts@tmXMajorGridThicknessF=0.3



plots = new(4,graphic)
res1=res
;res1@tiMainString = "1950_2014hwf-eof1"
res1@gsnLeftString  = "EOF1 "
;res1@cnLevelSelectionMode="ManualLevels"
;res1@cnMinLevelValF=1
;res1@cnMaxLevelValF=9.5
;res1@cnLevelSpacingF=1.5
;res1@cnFillColors=(/129,145,161,177,193,200,215,240/)

res1@gsnRightString = sprintf("%5.1f", eof@pcvar(0)) +"%"
plots(0) = gsn_csm_contour_map(wks,eof(0,:,:),res1)
res2=res
;res2@cnLevelSelectionMode="ManualLevels"
;res2@cnMinLevelValF=-4
;res2@cnMaxLevelValF=12
;res2@cnLevelSpacingF=2
;res2@cnFillColors=(/18,50,82,129,145,161,177,193,200,225/)
res2@gsnLeftString  = "EOF2"
res2@gsnRightString = sprintf("%5.1f", eof@pcvar(1)) +"%"
plots(1) = gsn_csm_contour_map(wks,eof(1,:,:),res2)
rts1=rts
rts1@tmXBMode = "Explicit"
rts1@tmXBValues=(/"0","10","20","30","40","50","60"/)
rts1@tmXBLabels=(/"1950","1960","1970","1980","1990","2000","2010"/)
rts1@tmXTOn="False"
rts1@tmYROn="False"
rts1@tmYLMode="Explicit"
rts1@tmYLValues=(/"-3","-2","-1","0","1","2","3"/)
rts1@tmYLLabels=(/"-3","-2","-1","0","1","2","3"/)
rts1@gsnLeftString  = "PC "+(0+1)
rts1@trYMinF=-3.5








;插入第一条曲线
yy1=new((64), "float")
yy1=1.96

yy2=new((64), "float")
yy2=-1.96

yy3=new((64), "float")
;yy3=asciiread("t1.txt",-1,"float")

yy4=new((64), "float")
;yy4=asciiread("t2.txt",-1,"float")

rts4=True
;rts4@xyLineColors       = (/"black"/) ; colors chosen
;rts4@xyLineThicknesses  = (/8./)      ; line thicknesses
;rts4@xyDashPatterns     = (/0./)      ; make all lines solid
rts4@gsLineDashPattern = 0.                    ; solid line
rts4@gsLineThicknessF  = 2.                    ; line thicker
rts4@gsLineColor       = "black"                 ; line color
rts4@tmYRMode="Explicit"
rts4@gsLineThicknessF   =5.
rts4@tmYRValues=(/"-2","-1","0","1","2"/)
rts4@tmYRLabels=(/"-2","-1","0","1","2"/)

rts5=rts4
rts5@xyDashPatterns     = (/5/)      ; make all lines solid 
rts5@gsLineDashPattern  =0

;;;;第一模态ts年际变化
ts11=eof_ts(0,:)
r11=runave_n(ts11, 9, 1, 0)   ;滤波
rts10=True
rts10@xyLineColors       = (/"black"/) ; colors chosen
rts10@xyLineThicknesses  = (/5./)      ; line thicknesses
rts10@xyDashPatterns     = (/0./)      ; make all lines solid
rts10@tmYRMode="Explicit"
rts10@gsLineThicknessF   =5.
rts10@tmYRValues=(/"-3","-2","-1","0","1","2","3","4"/)
rts10@tmYRLabels=(/"-3","-2","-1","0","1","2","3","4"/)


plots(2)= gsn_csm_xy(wks, time, eof_ts(0,:), rts1) 
dum20 = gsn_add_polyline(wks,plots(2),time,r11, rts10)  




rts6=rts5
rts6@gsLineColor       = "red"   



rts7=rts5
rts7@gsLineColor       = "black"   



;;;添加标志线
;;;;;;;;;;;;;;;;;;;;;;;;
res_text                    = True                  ; text mods desired
  res_text@txFontHeightF      = 0.015                 ; change text size
  res_text@txJust             = "CenterLeft"          ; text justification

  res_lines                   = True                  ; polyline mods desired
  res_lines@gsLineDashPattern = 0.                    ; solid line
  res_lines@gsLineThicknessF  = 5.                    ; line thicker
  res_lines@gsLineColor       = "black"                 ; line color
  d = (/1957,1962/)
  d2= (/1968,1973/)
  yyy = (/3.1,3.1/)
  ;dum6 = gsn_add_polyline(wks,plots(2),d,yyy,res_lines)              ; add polyline
  ;dum7 = gsn_add_text(wks,plots(2),"UB",1963,3.1,res_text); add text
  
  yyy = (/3.1,3.1/)
  res_lines@gsLineColor       = "red"                                 ; change to blue
  res_lines@gsLineDashPattern = 0.  
  ;dum8 = gsn_add_polyline(wks,plots(2),d2,yyy,res_lines)                ; add polyline
  ;dum9 = gsn_add_text(wks,plots(2),"UF",1974,3.1,res_text)       ; add text

  resline=True
  resline                   = True                  ; polyline mods desired
  resline@gsLineDashPattern = 0.                    ; solid line
  resline@gsLineThicknessF  = 3.                    ; line thicker
  resline@gsLineColor       = "black"                 ; line color

  d3= (/1951,2014/)
  yyy3 = (/1.96,1.96/)
  yyy4 =(/-1.96,-1.96/)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;























rts2=rts
rts2@tmXBMode = "Explicit"
rts2@tmXBValues=(/"0","10","20","30","40","50","60"/)
rts2@tmXBLabels=(/"1950","1960","1970","1980","1990","2000","2010"/)
rts2@tmXTOn="False"
rts2@tmYROn="False" 
rts2@tmYLMode="Explicit"
rts2@tmYLValues=(/"-2","-1","0","1","2"/)
rts2@tmYLLabels=(/"-2","-1","0","1","2"/)
rts2@trYMaxF=2.3 
rts2@gsnLeftString  = "PC "+(1+1)







;插入第二模态的平滑曲线

ts=eof_ts(1,:)
r=runave_n(ts, 9, 1,0)   ;滤波

rts3=True
rts3@xyLineColors       = (/"black"/) ; colors chosen
rts3@xyLineThicknesses  = (/5./)      ; line thicknesses
rts3@xyDashPatterns     = (/0./)      ; make all lines solid
rts3@tmYRMode="Explicit"
rts3@gsLineThicknessF   =5.
rts3@tmYRValues=(/"-2","-1","0","1","2"/)
rts3@tmYRLabels=(/"-2","-1","0","1","2"/)
;rts3@gsnYRefLine           = 0              ; reference line   

;fi=addfile("hwfits.nc", "c")
;fi->ts(0,:)=r11
;fi->ts(1,:)=r






plots(3)= gsn_csm_xy(wks, time, eof_ts(1,:),rts2) ;(wks,time,eof_ts(1,:),rts2)

dum2 = gsn_add_polyline(wks,plots(3),time,r, rts3)  



pres = True
;pres@tiMainString = "1950_2014hwf_eof"

pres@gsnMaximize = True
pres@gsnPanelDebug=True
pres@gsnPanelRowSpec = True 
pres@gsnPanelLabelBar = True
;pres@lbBoxLinesOn = False
pres@gsnPanelFigureStrings = (/"a","c","b","d"/)
pres@gsnPanelFigureStringsPerimOn  =False
pres@amJust  = "TopLeft"
pres@amZone =0.1
gsn_panel(wks,plots,(/2,2/),pres)



end  

  


