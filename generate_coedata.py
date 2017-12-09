# -*- coding = utf-8 -*-

WIDTH = 30      #ROM address width
DEPTH = 516     #ROM Depth

coe_data = ""
def cdata_strip(file_name):
    # read the data from the file
    file = open(file_name+".txt", 'rb')
    romdata = file.read()
    file.close()
    #data strip
    md_data = romdata.replace('\\0D\\0A', '').replace(' ', '')
    #data reordering
    global coe_data
    for i in range(0, DEPTH, 1):
        for j in range(0, WIDTH, 1):
            coe_data += md_data[i + j * DEPTH]
        coe_data += ('\n')
    coe_file = open(file_name + 'coe_22hdr.txt', 'wb')
    coe_file.write(coe_data)
    coe_file.close()




if __name__ == '__main__':
    print 'This is generate_coedata module'

