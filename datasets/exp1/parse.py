import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib as mpl


mpl.rcParams['font.sans-serif'] = ['SimHei']  # 中文
plt.rcParams['axes.unicode_minus'] = False    # 负号


path = 'data/train.txt'
data = pd.read_csv(path, index_col=0)


color = ['r', 'b']
for _, i in data.iterrows():
    x, y, c = i[0], i[1], color[int(i[2])-1]
    plt.scatter(x, y, color=c)
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.show()



