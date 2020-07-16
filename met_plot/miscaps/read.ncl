begin

f=addfile("test.nc", "r")
data =f->data
printVarSummary(data)

end