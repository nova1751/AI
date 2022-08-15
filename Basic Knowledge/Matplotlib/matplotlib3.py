#!/user/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rc("font", family='Microsoft YaHei')

y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
x = range(11,31)

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y,label="测试")

_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels)
plt.yticks(range(0,9))

plt.grid(alpha=0.1)
plt.legend()

plt.show()

# 1. 绘制了折线图(plt.plot)
# 2. 设置了图片的大小与分辨率(plt.figure())
# 3. 实现了图片的保存(plt.savefig)
# 4. 设置了x，y轴上的字符和刻度(xticks)
# 5. 解决了刻度稀疏和密集的问题(xticks)
# 6. 设置了标题，xy轴的标题(plt.title,plt.xlabel,plt.ylabel)
# 7. 设置了字体(matplotlib.rc())
# 8. 在一个图上绘制多个图形(plt多次plot即可)
# 9. 为不同的图形添加图例


