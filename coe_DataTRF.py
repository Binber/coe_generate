# -*- coding = utf-8 -*-

WIDTH = 30      #ROM address width
DEPTH = 516     #ROM Depth

#read the data from the file
file = open("coe_22hdr.txt",'rb')
coe_rvsfile = open("coe_22hdr_rvs.txt",'wb')
for line in file.readlines():
    #remove the space from start and end
    line_data = line.strip()
    #reverse the string
    line_datarvs = line_data[::-1]
    print line_datarvs
    #write data
    coe_rvsfile.write(line_datarvs+'\n')
file.close()
coe_rvsfile.close()



