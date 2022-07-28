#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

# ndarray对象的内容可以通过索引或切片来访问和修改，与 Python 中 list 的切片操作一样。
#
# ndarray 数组可以基于 0 - n 的下标进行索引，切片对象可以通过内置的 slice 函数，并设置 start, stop 及 step 参数进行，
# 从原数组中切割出一个新数组
a = np.arange(10)
s = slice(2, 7, 2)
print(a[s])

# 以上实例中，我们首先通过 arange() 函数创建 ndarray 对象。 然后，分别设置起始，终止和步长的参数为 2，7 和 2。
#
# 我们也可以通过冒号分隔切片参数 start:stop:step 来进行切片操作：
a = np.arange(10)
b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)

# 切片还可以包括省略号 …，来使选择元组的长度与数组的维度相同。 如果在行位置使用省略号，它将返回包含行中元素的 ndarray
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[...,1])
print(a[1,...])
print(a[...,1:])

