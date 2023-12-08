#通过0/1跳变预测仰卧起坐个数

#原始频为originvideo.mp4，实际仰卧起坐个数为20，跳变阈值为34,35,36最佳

import os
from fun import*
f = read_txt('result.txt')

same_cnt = 0
flag = 0
s = 50   #same_cnt,跳变的阈值,可调整
if os.path.exists("howmany.txt"):
        os.system("del howmany.txt")

for i in range(0,s+1):
    cnt = 0
    for line in f:
        line = line.strip('\n')
        data = line.split()
        data[2] = int(data[2])    
        if cnt==0:
            flag = data[2]
            cnt+=1
            continue
        if data[2] != flag and same_cnt>i-1 :
            same_cnt = 0
            cnt+=1      
            flag = data[2]
        if data[2] == flag:
            same_cnt+=1
    
    print(f'跳变阈值为{i},仰卧起坐个数为{cnt}个',file=open('howmany.txt','a'))
