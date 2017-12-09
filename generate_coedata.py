# -*- coding = utf-8 -*-

WIDTH = 30      #ROM address width
DEPTH = 516     #ROM Depth

def cdata_generate(file_name):
    # read the data from the file
    file = open(file_name+".txt", 'r')
    romdata = file.read()
    file.close()
    #data strip
    #print(romdata)
    md_data = romdata.replace("\\0D\\0A","").replace(" ", "")
    #data reordering
    coe_data = ""
    for i in range(0, DEPTH, 1):
        for j in range(0, WIDTH, 1):
            coe_data += md_data[i + j * DEPTH]
        coe_data += ('\n')

    #save format coe_data
    coe_file = open(file_name + '_coe.txt', 'w')
    coe_file.write(coe_data)
    #release coe_data
    coe_data = ""
    coe_file.close()

    # save reversed coe_data

    coe_rvsfile = open(file_name + '_coervs.txt', 'w')
    coefile = open(file_name + "_coe.txt", 'r')

    for line in coefile.readlines():
        #remove the space from start and end
        line_data = line.strip()
        #reverse coe_data
        line_rvsdata = line_data[::-1]
        #write data
        coe_rvsfile.write(line_rvsdata+'\n')

    coe_rvsfile.close()

    print ("Successfully")
if __name__ == '__main__':
    print ('This is generate_coedata module')
else:
    print ("Start Process")
