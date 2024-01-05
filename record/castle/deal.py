#计算两个时间节点间隔了多少秒
import time

import openpyxl
from datetime import datetime
import os
#读取castle.xlsx中的数据
import xlrd
data = xlrd.open_workbook('C:\\Users\\po1ar\\Desktop\\check\\castle.xlsx')
table = data.sheets()[0]
nrows = table.nrows
# print(table.row_values(0))
#['用户名', '打卡时间', '打卡事物', '打卡内容']
lis_a = []
lis_b = []
for i in range(1,nrows):
    row = table.row_values(i)
    if row[0]=='a':
        lis_a.append(row)
    if row[0]=='b':
        lis_b.append(row)
# print(lis_a)
# print(lis_b)
#将时间转化为秒,其中第一个时间节点设为0

def time_process(lis):
    time_start = (time.mktime(time.strptime(lis[0][1], "%Y-%m-%d %H:%M:%S")))%(1e8)
    new_lis = []
    new_lis.append([])
    round_now = 0
    for i in range(len(lis)):
        lis[i][1] = time.mktime(time.strptime(lis[i][1], "%Y-%m-%d %H:%M:%S"))
        lis[i][1]%=(1e8)
        lis[i][1]-=time_start
        if int(lis[i][2])==round_now+1:
            new_lis[round_now].append(lis[i][1])
            new_lis[round_now].append(lis[i][3])
        else:
            round_now+=1
            new_lis.append([])
            new_lis[round_now].append(lis[i][1])
            new_lis[round_now].append(lis[i][3])
    return new_lis
    # print(roundmax)
# print(time_process(lis_a))

def wave_speed(lis_x):
    secperwave=0
    delta_wave_time=[]
    sum=0
    for lis in lis_x:
        for i in range(0,len(lis),2):    
            for j in range(i+2,len(lis),2):
                delta_wave_time.append([int(lis[j+1])-int(lis[i+1]),lis[j]-lis[i]])
                sum+=lis[j]-lis[i]
    for i in delta_wave_time:
        # print(i)
        secperwave+=i[1]/i[0]*(i[1]/sum)
    return secperwave        


def gocastle(wavespeed):
    if not os.path.exists("C:/Users/po1ar/desktop/check/deal_log.xlsx"):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["秒/波","记录时间","1小时波数","1天波数","备注"])
        wb.save("C:/Users/po1ar/desktop/check/deal_log.xlsx")
    wb = openpyxl.load_workbook("C:/Users/po1ar/desktop/check/deal_log.xlsx")
    ws = wb.active
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ws.append([str(round(wavespeed,2)),log_time,str(round(3600/wavespeed,2)),str(round(24*3600/wavespeed,2))])
    wb.save("C:/Users/po1ar/desktop/check/deal_log.xlsx")
    

if __name__ == "__main__":
    lis_a = time_process(lis_a)
    wavespeed = wave_speed(lis_a)
    print(f'当前波速为  {round(wavespeed,2)}  秒/波')
    print(f'1小时内波数为  {round(3600/wavespeed,2)}  波')
    print(f'1天内波数为  {round(24*3600/wavespeed,2)}  波')
    gocastle(wavespeed)