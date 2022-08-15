#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy
import numpy as np

# numpy.empty
# numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
#
# numpy.empty(shape, dtype = float, order = 'C')
# 参数说明：
#
# 参数	描述
# shape	数组形状
# dtype	数据类型，可选
# order	有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
a = np.empty([3, 2], dtype=int)
print(a)

# numpy.zeros 创建指定大小的数组，数组元素用0来填充
# numpy.zeros(shape, dtype = float, order = 'C')
# 参数说明：
#
# 参数	描述
# shape	数组形状
# dtype	数据类型，可选
# order	'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组

# 默认为浮点数
x = np.zeros(5)
print(x)

# 设置类型为整数
y = np.zeros((5,), dtype=int)
print(y)

# 自定义类型
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)

# numpy.ones
# 创建指定形状的数组，数组元素以 1 来填充：
#
# numpy.ones(shape, dtype = None, order = 'C')
# 参数说明：
#
# 参数	描述
# shape	数组形状
# dtype	数据类型，可选
# order	'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组
# 默认为浮点数
x = np.ones(5)
print(x)

# 自定义类型
x = np.ones([2, 2], dtype=int)
print(x)