import os
def read_txt(path):
    f = open(path,'r')
    lines = f.readlines()
    f.close()
    return lines

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

    
#walk指定文件夹下所有.txt文件
def walk(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if os.path.splitext(file)[1] == ".txt":
                print(os.path.join(root, file))
