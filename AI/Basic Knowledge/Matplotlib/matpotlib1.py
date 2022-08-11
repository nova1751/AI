#!/user/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图
plt.plot(x, y)

# 设置x轴的刻度,同时注意不传入刻度就不会显示
_xtick_labels = [i / 2 for i in range(4, 49)]
plt.xticks(_xtick_labels[::3])
plt.yticks(range(min(y), max(y) + 1))

# 保存图片
# plt.savefig("./t1.png")

# 战士图形
plt.show()
