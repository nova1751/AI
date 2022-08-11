#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 线性回归（Linear Regression） 可能是最流行的机器学习算法。线性回归就是要找一条直线，并且让这条直线尽可能地拟合散点图中的数据点。
# 线性模型：给定由d个属性描述的示例，线性模型试图学得一个通过属性的线性组合来进行预测的函数。f(x) = wTx+b
#
# 线性回归试图学得一个线性模型以尽可能准确的预测实值输出标记，公式：
# f(xi) = wxi + b，使得f(xi) ≈ yi
#
# 我们的任务就是求出w和b，可用均方误差最小化的方法，基于均方误差最小化来进行模型求解的方法称为最小二乘法，在线性回归中，
# 最小二乘法就是试图找到一条直线，使得所有样本数据点到达直线的欧氏距离最小。总距离是所有数据点的垂直距离的平方和。
# 其思想是通过最小化这个平方误差或距离来拟合模型。
import numpy as np
from matplotlib import pyplot as plt


def fitSLR(X, Y):
    X_avg = np.mean(X)  # 求取括号内数组矩阵的均值
    Y_avg = np.mean(Y)
    n = len(X)  # 得到括号内列表长度即元素的个数
    # 定义分子与分母
    fen_zi = 0
    fen_mu = 0
    # 核心算法
    for i in range(0, n):
        fen_zi += (X[i] - X_avg) * (Y[i] - Y_avg)
        fen_mu += (X[i] - X_avg) ** 2
    b1 = fen_zi / float(fen_mu)  # 计算w，即直线的斜率
    b0 = Y_avg - b1 * X_avg
    return b0, b1


# 定义X,Y列表
X = [1.5, 0.8, 2.6, 1.0, 0.6, 2.8, 1.2, 0.9, 0.4, 1.3, 1.2, 2.0, 1.6, 1.8, 2.2]
Y = [3.1, 1.9, 4.2, 2.3, 1.6, 4.9, 2.8, 2.1, 1.4, 2.4, 2.4, 3.8, 3.0, 3.4, 4.0]

b0, b1 = fitSLR(X, Y)
print('w = ', b1)
print('b = ', b0)

# 生成画板
plt.figure()
# 画散点图
plt.scatter(X, Y)
X_min = min(X)
X_max = max(X)
Y_min = b0 + b1 * X_min
Y_max = b0 + b1 * X_max

plt.plot([X_min, X_max], [Y_min, Y_max], 'r')
plt.show()
