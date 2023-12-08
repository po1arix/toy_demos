import os
#依次读取merger_2下的文件，将非-1坐标用散点图画出来

import matplotlib.pyplot as plt

dir_path = "merger_3"
for file_name in os.listdir(dir_path):
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "r") as f:
        lines = f.readlines()
        x = []
        y = []
        for line in lines:
            coords = line.strip().split(" ")
            if coords[0] != "-1":
                x.append(float(coords[0]))
                y.append(float(coords[1]))
        plt.scatter(x, y)
        plt.show()



                