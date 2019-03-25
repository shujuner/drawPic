# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:49:29 2019

@author: kg
"""

import numpy as np
import matplotlib.pyplot as plt
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)  
size = 5
x = np.array([20,40,60,80])
a = np.array([8.1,5.9,4.3,3.7])
b = [5.7, 4.3, 2.1, 1.9]
c = np.random.random(size)

total_width, n = 8, 2
width = total_width / n
x = x - (total_width - width) / 2

plt.bar(x, a,  width=width, label='我们的聚类算法')
plt.bar(x + width, b, width=width, label='ClusStream')
#plt.bar(x + 2 * width, c, width=width, label='c')
plt.xlabel('K的数量')
plt.ylabel('误差平方和/10的八次方')

plt.title(u'准确率对比', FontProperties=font)
plt.legend()
plt.show()