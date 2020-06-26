begin
  NumXOut = 21
  NumYOut = 21
  ISLIM = 6

  x = (/0.00, 1.00, 0.00, 1.00, 0.40, 0.75/)
  y = (/0.00, 0.00, 1.00, 1.00, 0.20, 0.65/)
  z = (/0.00, 0.00, 0.00, 0.00, 1.25, 0.80/)

  xc = 1.d/(NumXOut-1.) 
  xi = ispan(0,NumXOut-1,1) * xc

  yc = 1.d/(NumYOut-1.) 
  yi = ispan(0,NumYOut-1,1) * yc

  zi = natgrid(x, y, z, xi, yi)

  ; Use natgrid_Wrap if metadata retention is desired
  ; zi = natgrid_Wrap(x, y, z, xi, yi)
end