#有用数据： lr_sho == neck , ave(wri,nose,eye,ear)
'''
elb
eye
ear
wri
sho
nose
neck
'''
from fun import read_txt,ana
import os
#sho,neck合并
sho = read_txt("merger_1/sho_1.txt")
neck = read_txt("merger_1/neck_1.txt")
with open("merger_2/snec_2.txt", 'w') as f:
    for i in range(len(sho)):
        sho_1 = sho[i].rstrip('\n')
        sho_1 = sho_1.split(' ')
        neck_1 = neck[i].rstrip('\n')
        neck_1 = neck_1.split(' ')
        if sho_1[0] != "-1":
            f.write(sho_1[0]+' '+sho_1[1]+'\n')
        elif neck_1[0] != "-1":
            f.write(neck_1[0]+' '+neck_1[1]+'\n')
        else:
            f.write("-1 -1\n")

print(ana("merger_2","ana_merge_2.txt"))

#ave合并
eye = read_txt("merger_1/eye_1.txt")
ear = read_txt("merger_1/ear_1.txt")
wri = read_txt("merger_1/wri_1.txt")
nose = read_txt("merger_1/nose_1.txt")
with open("merger_2/ave_2.txt", 'w') as f:
    for i in range(len(eye)):
        list_0 =[]
        list_1 =[]
        eye_1 = eye[i].rstrip('\n')
        eye_1 = eye_1.split(' ')
        ear_1 = ear[i].rstrip('\n')
        ear_1 = ear_1.split(' ')
        wri_1 = wri[i].rstrip('\n')
        wri_1 = wri_1.split(' ')
        nose_1 = nose[i].rstrip('\n')
        nose_1 = nose_1.split(' ')
        list_name = [eye_1,ear_1,wri_1,nose_1]
        for name in list_name:
            if name[0] != "-1":
                list_0.append(float(name[0]))
                list_1.append(float(name[1]))
        if len(list_0) != 0:
            f.write(str(int(sum(list_0)/len(list_0)))+' '+str(int(sum(list_1)/len(list_1)))+'\n')
        else:
            f.write("-1 -1\n")
#elb改名复制
os.system("copy merger_1\\elb_1.txt merger_2\\elb_2.txt")    #os.system("copy x y") 复制x文件并重命名为y  x和y都是路径 必须使用\\ 不能使用/

