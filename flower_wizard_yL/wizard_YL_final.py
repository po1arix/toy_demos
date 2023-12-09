import cv2
plant = cv2.VideoCapture('plant.mp4')
wizard_self = cv2.VideoCapture('wizard_self.mp4')
count = 0   #减去抖音片头
start = 95
count_2 = 0  #YL法师抬手前摇
start_2 = 20
count_3 = 0 #减去YL法师露馅部分
end = 90
while True:
    bool_p, plantframe = plant.read()
    if bool_p:
        if count < start:
            count += 1
            continue
        bool_w, wizardframe = wizard_self.read()
        if not bool_w or count_3 == end:
            cv2.waitKey(0)  # 片尾定格
            break
        wizardframe = cv2.resize(wizardframe, (360, 600))
        if count_2 > start_2:
            plantframe = cv2.resize(plantframe,(360,600))
            plantframe = plantframe[plantframe.shape[0]//2:]
            ph,pw,pc = plantframe.shape
            wh,ww,wc = wizardframe.shape
            d = wh-ph
            for x in range(ww):            
                for y in range(wh):
                    if y>d:
                        pf = plantframe[y-d,x].tolist()
                        if pf[0] in range(256) and pf[1] in range(60) and pf[2] in range(70):       #256 60 70
                            continue
                        wizardframe[y,x] = plantframe[y-d,x]
        count_2 += 1
        count_3 += 1
        wizardframe = wizardframe[:wizardframe.shape[0]-100,:,:]
        wizardframe = cv2.resize(wizardframe, (360, 600))
        cv2.imshow('magic',wizardframe)
        cv2.waitKey(1)