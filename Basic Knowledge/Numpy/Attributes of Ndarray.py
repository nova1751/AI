#!/user/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# ndarray.ndim 用于返回数组的维数，也就是数组的秩
a = np.arange(24)
print(a.ndim)  # a现在只有一个维度
# 现在调整其大小
b = a.reshape(2, 4, 3)  # b现在有三个维度
print(b.ndim)

# ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性(秩)。比如，一个二维数组，
# 其维度表示"行数"和"列数"。
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c.shape)
# ndarray.shape 也可以用于调整数组大小。
d = c
d.shape = (3, 2)
print(d)
# NumPy 也提供了 reshape 函数来调整数组大小
e = c.reshape(3, 2)
print(e)

# ndarray.itemsize 以字节的形式返回数组中每一个元素的大小。
# 例如，一个元素类型为 float64 的数组 itemsize 属性值为 8(float64 占用 64 个 bits，每个字节长度为 8，所以 64/8，占用 8 个字节），
# 又如，一个元素类型为 complex32 的数组 item 属性为 4（32/8）。

# 数组的dtype为int8(一个字节)
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)

# 数组的 dtype 现在为float64(8个字节)
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(y.itemsize)

# ndarray.flags
# ndarray.flags 返回 ndarray 对象的内存信息，包含以下属性：
# 属性	描述
# C_CONTIGUOUS (C)	数据是在一个单一的C风格的连续段中
# F_CONTIGUOUS (F)	数据是在一个单一的Fortran风格的连续段中
# OWNDATA (O)	数组拥有它所使用的内存或从另一个对象中借用它
# WRITEABLE (W)	数据区域可以被写入，将该值设置为 False，则数据为只读
# ALIGNED (A)	数据和所有元素都适当地对齐到硬件上
# UPDATEIFCOPY (U)	这个数组是其它数组的一个副本，当这个数组被释放时，原数组的内容将被更新
m = np.array([1, 2, 3, 4, 5])
print(m.flags)
