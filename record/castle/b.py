
import openpyxl
from datetime import datetime
import os
def gocastle(username):
    if not os.path.exists("C:/Users/po1ar/desktop/check/castle.xlsx"):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["用户名","打卡时间","打卡事物","打卡内容"])
     
        wb.save("C:/Users/po1ar/desktop/check/castle.xlsx")
    wb = openpyxl.load_workbook("C:/Users/po1ar/desktop/check/castle.xlsx")
    ws = wb.active
    castle = input("请输入打卡事物：")
    castle_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    castle_content = input("请输入打卡内容，数字用英文句号隔开：")
    ws.append([username,castle_time,castle,castle_content])
    wb.save("C:/Users/po1ar/desktop/check/castle.xlsx")
    print("打卡成功！")


admin_list = ['a','test','b']
username = input("请输入用户名：")

if username not in admin_list: 
    password = input("请输入密码：")
flag = False
if os.path.exists("C:/Users/po1ar/desktop/check/user.txt"):  
    f = open("C:/Users/po1ar/desktop/check/user.txt", "r", )
    txt = f.readlines()
    for line in txt:
        line = line.strip()
        if line == "":
            continue
        ur,pw = line.split(",")
        if ur == username and pw == password or username in admin_list:
            flag = True
            break
if flag:
    gocastle(username)
     
