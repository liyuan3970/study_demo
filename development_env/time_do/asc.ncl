begin
ncol = 10
data = readAsciiTable("tpyrced_20061920.006", ncol, "float", 2)
;x1 = asciiread("tpyrced_20061920.006" , , "float")
printVarSummary(data)
print(data(0,1))
end