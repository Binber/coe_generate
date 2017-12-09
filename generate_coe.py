# -*- coding = utf-8 -*-

WIDTH = 30      #ROM address width
DEPTH = 516     #ROM Depth

#read the data from the file
file = open("22_HDR.txt",'rb')
romData = file.read()
file.close()

#replace '\0D\0A' with '\n' and remove space
md_data = romData.replace('\\0D\\0A','').replace(' ','')

coe_data = ""

for i in range(0,DEPTH,1):
    for j in range(0,WIDTH,1):
        coe_data += md_data[i+j*DEPTH]
    coe_data +=('\n')

print coe_data

coe_file = open('coe_22hdr.txt','wb')
coe_file.write(coe_data)
coe_file.close()

