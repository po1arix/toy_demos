import cv2
plant = cv2.VideoCapture('plant.mp4')
wizard_self = cv2.VideoCapture('wizard_self.mp4')
count = 0   #减去抖音片头
start = 95
count_2 = 0  #YL法师抬手前摇
start_2 = 20
count_3 = 0 #减去YL法师露馅部分
end = 90

# def readbackground(txt):
#     back_ground = []
#     f=open(txt,'r')
#     lines =f.readlines()
#     f.close()
#     for line in lines:
#         back_ground.append(line[:-1])
#     return back_ground

# real_back = readbackground('back_ground.txt')# real_back = readbackground('back_ground.txt')

# 效果不错但,过于变态
# def background_generate():
#     real_back = []
#     for i in range(200,250):
#         for j in range(0,30):
#             for z in range(16):
#                 real_back.append(str([i, z, j]))
#     return real_back
#
# real_back = background_generate()

# def bg(origin):
#     background = []
#     for i in origin:
#         if i not in background:
#             background.append(i)
#     return background

while True:
    bool_p, plantframe = plant.read()
    if bool_p:
        if count < start:
            count += 1
            continue
        bool_w, wizardframe = wizard_self.read()
        if not bool_w or count_3 == end:
            cv2.waitKey(0) # 片尾定格
            break
        wizardframe = cv2.resize(wizardframe, (360, 600))
        if count_2 > start_2:
            plantframe = cv2.resize(plantframe, (360, 600))
            plantframe = plantframe[plantframe.shape[0] // 2:]

            # print(wizardframe.shape,plantframe.shape)

            # print(type(plantframe[10,180]))

            # for i in range(10):   #暴力读取背景
            #     background.append(plantframe[i,180].tolist())

            ph,pw,pc = plantframe.shape
            wh,ww,wc = wizardframe.shape
            d = wh-ph
            for x in range(ww):
                for y in range(wh):
                    if y>d:
                        # if str(plantframe[y-d,x].tolist()) in real_back:  搭配line 14/26
                        pf = plantframe[y-d,x].tolist()
                        if pf[0] in range(300) and pf[1] in range(60) and pf[2] in range(70):       #300 60 70
                            continue
                        wizardframe[y,x] = plantframe[y-d,x]
        count_2 += 1
        count_3 += 1
        wizardframe = wizardframe[:wizardframe.shape[0]-100,:,:]
        wizardframe = cv2.resize(wizardframe, (360, 600))
        cv2.imshow('magic',wizardframe)
        cv2.waitKey(1)
#末尾废料
# back = bg(background)
# print(back)
# cnt = 0
# for list in back:
#         print(list,file=open("back_ground.txt",'a'))

# 废料堆
# plant_h = int(plant.get(3))
# plant_w  = int(plant.get(4))
# wizard_self_h = int(wizard_self.get(3))
# wizard_self_w = int(wizard_self.get(4))
# print(plant_h,plant_w,wizard_self_h,wizard_self_w)
# 720 1280 1080 1920

# 很遗憾str不能这么玩

# def back_ground():
#     if os.path.exists("back_ground.txt"):
#         os.system('del back_ground.txt')
#     f = open("back_ground.txt",'wt',encoding='UTF-8')
#     f.close()

# 很遗憾数组不能这么玩,需要改一下玩法

# back_ground_origin =[]
# def  bg(origin):
#     background = []
#     for- 1i in origin:
#         if i not in background:
#             background.append(i)
#     return background
