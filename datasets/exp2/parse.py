import os
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib as mpl
from PIL import Image
import numpy as np
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 中文
plt.rcParams['axes.unicode_minus'] = False    # 正负号


c_path = './cloud/'
f_path = './forest/'

c_name = [c_path + i for i in os.listdir(c_path)]
f_name = [f_path + i for i in os.listdir(f_path)]

def show_grey(root=c_name):
    for n, i in enumerate(c_name):
        plt.subplot(2, 5, n+1)
        img = Image.open(i)
        img = img.convert('L')           #转为灰度图
        plt.imshow(img)
        plt.axis('off')
    plt.show()

def get_mat(root=c_name):
    for n, i in enumerate(c_name):
        plt.subplot(2, 5, n+1)
        img = Image.open(i)
        img = img.convert('L')            #转为灰度图
        img = np.array(img)               #转为ndarray
        yield img


for i in get_mat():
    print(i)

show_grey()