#随机生成x,y，x,y均服从正态分布，
#x属于(500,1200)且y属于(100,450),z=0
#x属于[1200，1500)且y属于[450,650),z=1
#生成的80%数据保存在sport_train.txt中
#生成的20%数据保存在sport_val.txt中
import numpy as np
import os 
os.makedirs('demo/dataset', exist_ok=True)
ftrain = open('demo/dataset/sport_train.txt', 'wt')
fval = open('demo/dataset/sport_val.txt', 'wt')

x = np.random.normal(1350, 150, (100,))
y = np.random.normal(550, 100, (100,))
for i in range(80):
    ftrain.write(f'{x[i]} {y[i]} 1\n')
for i in range(80, 100):
    fval.write(f'{x[i]} {y[i]} 1\n')

x = np.random.normal(850, 350, (100,))
y = np.random.normal(275, 175, (100,))
for i in range(80):
    ftrain.write(f'{x[i]} {y[i]} 0\n')
for i in range(80, 100):
    fval.write(f'{x[i]} {y[i]} 0\n')

ftrain.close()
fval.close()