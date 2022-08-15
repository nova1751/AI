#!/user/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

# Pandas 数据结构 - Series
# Pandas Series 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型。
#
# Series 由索引（index）和列组成，函数如下：
#
# pandas.Series( data, index, dtype, name, copy)
# 参数说明：
#
# data：一组数据(ndarray 类型)。
#
# index：数据索引标签，如果不指定，默认从 0 开始。
#
# dtype：数据类型，默认会自己判断。
#
# name：设置名称。
#
# copy：拷贝数据，默认为 False。
#
# 创建一个简单的 Series 实例：
a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar)
# 从上图可知，如果没有指定索引，索引值就从 0 开始，我们可以根据索引值读取数据：

a = ["Google", "Runoob", "Wiki"]

myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)

# 我们也可以使用 key/value 对象，类似字典来创建 Series：
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites)

print(myvar)
# 从上图可知，字典的 key 变成了索引值。

# 如果我们只需要字典中的一部分数据，只需要指定需要数据的索引即可，如下实例：
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites, index=[1, 2])

print(myvar)

# 设置 Series 名称参数：
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites, index=[1, 2], name="RUNOOB-Series-TEST")

print(myvar)
