# 数据类型对象
# 使用标量类型
import numpy as np

a = np.dtype(np.int64)
print(a)

# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
b = np.dtype('i4')
print(b)

# 字节顺序标注
c = np.dtype('<i4')
print(c)

# 结构化数据类型
d = np.dtype([('age', np.int8)])
print(d)

# 将数据结构类型应用至ndarray对象
e = np.array([(10,), (20,), (30,)], dtype=d)
print(e)

# 类型字段名可用于存取实际的 age 列
print(e['age'])

# 下面的示例定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)

a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a)
