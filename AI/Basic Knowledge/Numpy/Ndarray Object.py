import numpy

# 使用列表构建一维数组
import numpy as np

a = numpy.array([1, 2, 3])
print(a)
print(type(a))

# 使用列表构建二维数组
b = numpy.array([[1, 2, 3], [4, 5, 6]])
print(b)

# 可设置dtype来改变数组元素的数据类型
c = numpy.array([1, 2, 3, 4], dtype=complex)
print(c)

# 通过ndim查看数组的维度
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(arr.ndim)

# 通过ndmin创建不同维度的数组
arr1 = np.array([1, 2, 3, 4, 5], ndmin=2)
print(arr1)

# reshape数组变维
arr2 = np.array([[1, 2], [3, 4], [5, 6]])
print(arr2)
arr2 = arr2.reshape(2, 3)
print(arr2)
