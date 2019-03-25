# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:25:03 2019

@author: kg
"""
#coding:utf-8

from matplotlib import pyplot
import matplotlib.pyplot as plt
 
names = ['Soy','Iris','Wine','Sega','Iono']
#names = [str(x) for x in list(names)]
plt.rcParams['font.sans-serif']=['SimHei']
x = names
y_train = [91,93,92,77,75]
y_test  = [63,58,39,60,58]
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围
 
 
plt.plot(x, y_train, marker='o', mec='r', mfc='w',label=u'我们的方法')
plt.plot(x, y_test, marker='*', ms=10,label='传统K-means')
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=1)
 
plt.margins(0)
plt.subplots_adjust(bottom=0.10)
plt.xlabel('UCI 数据集') #X轴标签
plt.ylabel("准确率 / %") #Y轴标签
pyplot.yticks([0,25,50,75,100])
#plt.title("A simple plot") #标题
plt.savefig('F:\\f1.jpg',dpi = 900)
