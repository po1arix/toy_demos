import os 
from fun import *
#ave_2与snec_2合并
ave = read_txt("merger_2/ave_2.txt")
snec = read_txt("merger_2/snec_2.txt")
with open("merger_3/head_3.txt", 'w') as f:
    for i in range(len(ave)):
        ave_1 = ave[i].rstrip('\n')
        ave_1 = ave_1.split(' ')
        snec_1 = snec[i].rstrip('\n')
        snec_1 = snec_1.split(' ')
        list = [0,0,0]
        if ave_1[0] != "-1":
            list[0] += float(ave_1[0])
            list[1] += float(ave_1[1])
            list[2]+=1
        if snec_1[0] != "-1":
            list[0] += float(snec_1[0])
            list[1] += float(snec_1[1])
            list[2]+=1
        if list[2] != 0:
            f.write(str(int(list[0]/list[2]))+' '+str(int(list[1]/list[2]))+'\n')
        else:
            f.write("-1 -1\n")
    
ana("merger_3","ana_merge_3.txt")