#!/user/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import random
import matplotlib

# 防止中文乱码
matplotlib.rc("font", family='Microsoft YaHei')

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)

# 调整x轴的刻度
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45)

# 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度 单位(℃)")
plt.title("10点到12点每分钟的气温变化情况")

plt.show()
