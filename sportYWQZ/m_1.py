#读取origin_data文件夹下txt文件，对应的部位l，r合并 如将l_ear.txt和r_ear.txt合并为ear_1.txt
#将合并后的文件存放在merger_data文件夹下
import os

#读取文件夹dir下所有txt文件，统计-1数量，生成{new_filename}.txt
def ana(dir,new_filename):
    with open(new_filename,'wt') as f2:
        for root, dirs, files in os.walk(dir):
            for file in files:
                if os.path.splitext(file)[1] == ".txt":
                    f = open(os.path.join(root, file), 'r')
                    lines = f.readlines()
                    f.close()
                    count = 0
                    for line in lines:
                        line = line.rstrip('\n')
                        line = line.split(' ')
                        if line[0] == "-1":
                            count += 1
                    f2.write(dir+'/'+file+'\t'+str(count)+'\n')               
# ana("origin_data","ana_1.txt")

    
    
#walk指定文件夹下所有.txt文件
def walk(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if os.path.splitext(file)[1] == ".txt":
                print(os.path.join(root, file))



#读取ana_1.txt
def read_txt(path):
    f = open(path,'r')
    lines = f.readlines()
    f.close()
    return lines

#print(read_txt("ana_1.txt"))

#无用的-1数字典
# dic_minus_1 = {}
# ana_1 = read_txt("ana_1.txt")
# for s in ana_1:
#     s = s.lstrip('origin_data/')
#     s = s.rstrip('\n')
#     s = s.split('.txt\t')
#     dic_minus_1[s[0]] = s[1]
# print(dic_minus_1)

#把身体部位名字读出来
name_list = ['l_ank', 'l_ear', 'l_elb', 'l_eye', 'l_hip', 'l_knee', 'l_sho', 'l_wri', 'neck', 'nose', 'r_ank', 'r_ear', 'r_elb', 'r_eye', 'r_hip', 'r_knee', 'r_sho', 'r_wri']
# ana_1 = read_txt("ana_1.txt")
# for i in ana_1:
#     i = i.split('.txt')
#     for j in range(len(i[0])):
#         if i[0][j] == '/':
#             name_list.append(i[0][j+1:])
#             break
# print(name_list)
        
#身体部位进行lr配对
couple_list = [['l_ank', 'r_ank'], ['l_ear', 'r_ear'], ['l_elb', 'r_elb'], ['l_eye', 'r_eye'], ['l_hip', 'r_hip'], ['l_knee', 'r_knee'], ['l_sho', 'r_sho'], ['l_wri', 'r_wri']]
# for name in name_list:
#     if name[0] == 'l':
#         couple_list.append(['l_'+name[2:], 'r_'+name[2:]])
# print(couple_list)

#将l和r合并,近似生成新部位坐标文件，存放在merger_1下(不包括neck和nose)(不包括-1)
for cp in couple_list:
        left = read_txt("origin_data\\"+cp[0]+".txt")
        right = read_txt("origin_data\\"+cp[1]+".txt")
        with open("merger_1\\"+cp[0][2:]+"_1.txt", 'w') as f:
            for i in range(len(left)):   #left和right的长度相同
                left_1 = left[i].rstrip('\n')
                left_1 = left_1.split(' ')
                right_1 = right[i].rstrip('\n')
                right_1 = right_1.split(' ')
                # print(left_1)
                if left_1[0] != "-1":            #有效情况下优先取left_1
                    f.write(left_1[0]+' '+left_1[1]+'\n')
                elif right_1[0] != "-1":         #left_1无效时取right_1
                    f.write(right_1[0]+' '+right_1[1]+'\n')
                else:                            #都无效时取-1
                    f.write("-1 -1\n")
        f.close()
#复制nose和neck并重命名为nose_1和neck_1加入merger_1
os.system("copy origin_data\\nose.txt merger_1\\nose_1.txt")
os.system("copy origin_data\\neck.txt merger_1\\neck_1.txt")    #os.system("copy x y") 复制x文件并重命名为y  x和y都是路径 必须使用\\ 不能使用/

ana("merger_1","ana_merge_1.txt")

list_1 =[]

ana_merge_1 = read_txt("ana_merge_1.txt")
for s in ana_merge_1:
    s = s.rstrip('\n')
    s = s.split('\t')
    list_1.append(s)
#冒泡排序-1个数
for i in range(len(list_1)):
    for j in range(len(list_1)-i-1):
        if int(list_1[j][1]) > int(list_1[j+1][1]):
            list_1[j],list_1[j+1] = list_1[j+1],list_1[j]
for i in list_1:
    print(i[0],i[1])

