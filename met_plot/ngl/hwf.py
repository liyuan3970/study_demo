from netCDF4 import Dataset
import numpy as np
import Ngl

f1 = Dataset('hwfe.nc')
f2 = Dataset('hwfts.nc')

lons = f1.variables['lon'][:]
lats = f1.variables['lat'][:]
eof = f1.variables['e'][1,:,:]


ts = f2.variables['ts'][:]

rlist    = Ngl.Resources()

wks = Ngl.open_wks("png","contour",rlist)

res=rlist
#res.gsnDraw = False
#res.gsnFrame = False
#res.gsnAddCyclic        = False
res.mpCenterLonF         = 100  
res.mpLimitMode       = "LatLon"
res.mpMinLatF         = 15         
res.mpMaxLatF         = 55
res.mpMinLonF         = 70
res.mpMaxLonF         = 140
res.cnFillOn       = True
#res.cnFillPattern ="Explicit"

res.mpFillOn              = True     #turn on color fill
res.mpDataSetName         = "Earth..4"
res.mpDataBaseVersion     = "MediumRes"
#res.mpAreaMaskingOn       = True
res.mpMaskAreaSpecifiers  = ["China","taiwan"]
res.mpOutlineSpecifiers   = ["China"]

res.mpLandFillColor            = "white"
res.mpInlandWaterFillColor     = "white"
res.mpOceanFillColor           = "white"
res.mpFillBoundarySets         = "NoBoundaries"
res.mpOutlineBoundarySets      = "NoBoundaries"
res.mpNationalLineColor        = "black"
res.mpProvincialLineColor      = "black"
res.mpGeophysicalLineColor     = "black"
res.mpNationalLineThicknessF   = 2
res.mpProvincialLineThicknessF = 1

res.lbBoxLinesOn          =False

res.cnFillOn              = True
res.cnFillDrawOrder       = "PreDraw"
res.cnLineLabelsOn        = False
res.cnLinesOn             = True    # turn of contour lines
res.cnLineDrawOrder       = "PreDraw"
#res.cnLevelSpacingF       = 0.5      ; contour spacing
#res.lbLabelAutoStride          = True
res.lbLabelBarOn = False
res.pmTickMarkDisplayMode = "Always"
res.cnSmoothingOn      =True
res.cnSmoothingDistanceF = 0.01
res.cnSmoothingTensionF = -1.5
res.cnRasterSmoothingOn= True

res.tmXBMode = "Explicit"
res.tmXBValues = ["70","80","90","100","110","120","130","140"]
res.tmXBLabels  = ["70E","80E", "90E", "100E","110E","120E","130E","140E"]

res.cnMissingValFillColor="white"
res.vpXF = 0    #左边距
res.vpYF = 0.95     #上边距
res.vpWidthF  = 0.8             #height and width of plot
res.vpHeightF = 0.8
res.tmXBLabelFontHeightF  = 0.02
res.tmYLLabelFontHeightF  = 0.02
res.cnLevelSelectionMode="ManualLevels"
res.cnMinLevelValF=-4
res.cnMaxLevelValF=12
res.cnLevelSpacingF=2
res.cnFillColors=[18,50,114,129,145,161,177,193,200,215,240]


#map = Ngl.map(wks,res)
#Ngl.maximize_plot(wks,map)
print(dir(Ngl))
contour = Ngl.contour_map(wks,eof,res)

