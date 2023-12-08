import cv2
y = cv2.imread('yl.jpg')
q = cv2.imread('qian.jpg')
q = cv2.resize(q,(160,160))
rq = cv2.flip(q,1)
rq = cv2.resize(rq,(160,140))
M = cv2.getRotationMatrix2D((80,70),-85,1)  #-85是顺时针旋转85度
rq = cv2.warpAffine(rq,M,(160,140),borderValue=(255,255,255)) #旋转后的图像大小不变，白色填充
y = cv2.resize(y,(400,600))
for i in range(330,430):# 把y的左手替换为周边布料颜色从左借颜色，向右黏贴，友情提示：lbl立大功了
    for j in range(200,300):
        y[i,j] = y[i,j-10]       
qh,qw,qc = q.shape
rqh,rqw,rqc = rq.shape
yh,yw,yc = y.shape
s_h1 = 475
s_w1 = 115
for x_1 in range(qw): #左蟹钳         
    for y_1 in range(qh):
            zuo = q[y_1,x_1].tolist()
            if zuo[0]>230 and zuo[1]>230 and zuo[2]>230: #去除白色背景 ，不设置为255是为了把蟹钳边缘的白色也去掉    
                continue
            if x_1+s_w1>=yw or y_1+s_h1>=yh: #防止越界
                continue
            if 90<y[y_1+s_h1,x_1+s_w1][2]<135 and x_1<25: #蟹钳与讲台的交界处修缮
                 continue
            y[y_1+s_h1,x_1+s_w1] = q[y_1,x_1]
s_h2 = 323#右蟹钳
s_w2 = 170
for x_2 in range(rqw):          
    for y_2 in range(rqh):
            you = rq[y_2,x_2].tolist()
            if you[0]>230 and you[1]>230 and you[2]>230: #去除白色背景 ，不设置为255是为了把蟹钳边缘的白色也去掉
                continue
            if x_2+s_w2>=yw or y_2+s_h2>=yh:
                continue
            if x_2+s_w2 in range(270,300) and y_2+s_h2 in range(450,460):
                y[y_2+s_h2,x_2+s_w2] = y[y_2+s_h2,x_2+s_w2-10] 
                continue
            if x_2+s_w2 in range(200,250) and y_2+s_h2 in range(450,470):
                y[y_2+s_h2,x_2+s_w2] = [52,56,45] #下左瑕疵
                continue
            if x_2+s_w2 in range(200,350) and y_2+s_h2 in range(450,460): #右蟹钳下边缘与袖口的修缮
                b,g,r = y[y_2+s_h2,x_2+s_w2]
                if b<60 and g<60 and r<60:
                    continue
            y[y_2+s_h2,x_2+s_w2] = rq[y_2,x_2]
cv2.imshow('Ant_claw is AC , krabby_boyo is KB.', y)
cv2.waitKey(0)