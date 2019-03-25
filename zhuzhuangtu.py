# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:36:19 2019

@author: kg
"""

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)  

plt.bar([1, 3, 5, 7], [19, 23, 50, 68], label='我们的聚类算法')

plt.bar([2, 4, 6, 8], [18, 20, 47, 65], label='ClusStream')

# params

# x: 条形图x轴
# y：条形图的高度
# width：条形图的宽度 默认是0.8
# bottom：条形底部的y坐标值 默认是0
# align：center / edge 条形图是否以x轴坐标为中心点或者是以x轴坐标为边缘

plt.legend()

plt.xlabel('K的数量')
plt.ylabel('误差平方和')

plt.title(u'运行时间对比', FontProperties=font)

plt.show()
