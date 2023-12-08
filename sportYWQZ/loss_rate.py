import os

#sumtxt为任意包含某个身体部位所以坐标的txt文件，testtxt为处理好的统计各部位-1行数的txt文件
def loss_rate(sumtxt,testtxt):
    sum = len(open(sumtxt,'r').readlines())
    print('-'*50,'\n',file = open("sum.txt",'a'))
    print(testtxt,'\t','loss_rate:','\n',file = open("sum.txt",'a'))
    test = open(testtxt,'r').readlines()  
    ans = []
    dic = {}
    for line in test:
        line = line.rstrip('\n')
        line = line.split('\t')
        if line[1] != '0':
            ans.append(round(float(line[1])/sum*100,10))
            dic[round(float(line[1])/sum*100,10)] = line[0].split('/')[-1]
            # print(line[0].split('/')[-1],'\t','的丢失率为','\t',round(float(line[1])/sum,8)*100,'%')
    ans.sort()
    for i in ans:
        print(dic[i],'\t\t','loss_rate:','\t',i,'%',file = open("sum.txt",'a'))

if __name__ == "__main__":
    #如果存在sum.txt则删除
    if os.path.exists("sum.txt"):
        os.system("del sum.txt")
    loss_rate("origin_data\\l_ank.txt","ana_1.txt")
    loss_rate("origin_data\\l_ank.txt","ana_merge_1.txt")
    loss_rate("origin_data\\l_ank.txt","ana_merge_2.txt")
    loss_rate("origin_data\\l_ank.txt","ana_merge_3.txt")