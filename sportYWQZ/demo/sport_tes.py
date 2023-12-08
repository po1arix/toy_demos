import torch
from torch.autograd import Variable
from train_sport import SportNet
import numpy as np

use_cuda = False
model = SportNet()
model.load_state_dict(torch.load('output/params_95.pth'))  #params_xx.pth任意选择一个
model.eval()

f,f2 = open('dataset/head_3.txt', 'r'),open('result.txt','w')   #f为待预测的数据集，f2为预测结果

for line in f:
    line = line.strip('\n')
    data = line.split()
    if data[0] and data[1] == '-1':
        continue
    olddata = data
    data_tensor = torch.FloatTensor([float(data[0])/1500.0,float(data[1])/700.0])
    data_tensor = data_tensor.unsqueeze(0)
    prediction = model(Variable(data_tensor))
    pred = torch.max(prediction, 1)[1]
    predy = pred.data.numpy()
    if predy == 0:
        print(olddata[0],olddata[1],"0",file=f2,sep='\t')
    else:
        print(olddata[0],olddata[1],"1",file=f2,sep='\t')
f.close()  
f2.close()
#1为立，0为躺