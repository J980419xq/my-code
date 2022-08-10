import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#读取数据
#datafile = u'D:\\pythondata\\learn\\matplotlib.xlsx'
#data = pd.read_excel(datafile)
#box_1, box_2, box_3, box_4 = data[''], data['收入_JJ'], data['收入_Jolin'], data['收入_Hannah']
all_data=[np.random.normal(0,std,100) for std in range(1,4)] #模拟数据
fig, ax = plt.subplots()
ax.set_xlabel('x label') #设置x轴名称 x label
ax.set_ylabel('y label') #设置y轴名称 y label
plt.title('Examples of boxplot',fontsize=20)#标题，并设定字号大小
labels = 'Jay','JJ','Jolin'#图例
ax.boxplot(all_data,labels=labels,patch_artist=True)
plt.show()#显示图像