from re import M
from tkinter.ttk import LabeledScale
import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd

# 0.准备x, y坐标的数据
#读取数据
#datafile = u'D:\\pythondata\\learn\\matplotlib.xlsx'
#data = pd.read_excel(datafile)
matrix=[
    [0,1,2,3,4],
    [0,1,4,9,16],
    [0,1,8,27,64]
]
Labels=["a","b"]
# 1.创建画布,x轴记号,y轴记号
fig, ax = plt.subplots()
plt.xticks( matrix[0])
plt.yticks([i*10 for i in range(7)])
ax.set_xlabel('x label') #设置x轴名称 x label
ax.set_ylabel('y label') #设置y轴名称 y label
# 2.绘制折线图
for i in range(1,len(matrix)):
    ax.plot(matrix[0],matrix[i],label=Labels[i-1])
ax.set_title('Simple Plot') #设置图名为Simple Plot
ax.legend() #自动检测要在图例中显示的元素，并且显示
# 3.显示图像
plt.show()