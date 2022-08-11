#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

# NumPy 排序、条件刷选函数
# NumPy 提供了多种排序的方法。 这些排序函数实现不同的排序算法，每个排序算法的特征在于执行速度，最坏情况性能，所需的工作空间和算法的
# 稳定性。 下表显示了三种排序算法的比较。
#
# 种类	速度	最坏情况	工作空间	稳定性
# 'quicksort'（快速排序）	1	O(n^2)	0	否
# 'mergesort'（归并排序）	2	O(n*log(n))	~n/2	是
# 'heapsort'（堆排序）	3	O(n*log(n))	0	否
# numpy.sort()
# numpy.sort() 函数返回输入数组的排序副本。函数格式如下：
#
# numpy.sort(a, axis, kind, order)
# 参数说明：
#
# a: 要排序的数组
# axis: 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序， axis=0 按列排序，axis=1 按行排序
# kind: 默认为'quicksort'（快速排序）
# order: 如果数组包含字段，则是要排序的字段
a = np.array([[3,7],[9,1]])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 sort() 函数：')
print (np.sort(a))
print ('\n')
print ('按列排序：')
print (np.sort(a, axis =  0))
print ('\n')
# 在 sort 函数中排序字段
dt = np.dtype([('name',  'S10'),('age',  int)])
a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)
print ('我们的数组是：')
print (a)
print ('\n')
print ('按 name 排序：')
print (np.sort(a, order =  'name'))

# numpy.argsort()
# numpy.argsort() 函数返回的是数组值从小到大的索引值。
x = np.array([3,  1,  2])
print ('我们的数组是：')
print (x)
print ('\n')
print ('对 x 调用 argsort() 函数：')
y = np.argsort(x)
print (y)
print ('\n')
print ('以排序后的顺序重构原数组：')
print (x[y])
print ('\n')
print ('使用循环重构原数组：')
for i in y:
    print (x[i], end=" ")

# numpy.lexsort()
# numpy.lexsort() 用于对多个序列进行排序。把它想象成对电子表格进行排序，每一列代表一个序列，排序时优先照顾靠后的列。
#
# 这里举一个应用场景：小升初考试，重点班录取学生按照总成绩录取。在总成绩相同时，数学成绩高的优先录取，在总成绩和数学成绩都相同时，
# 按照英语成绩录取…… 这里，总成绩排在电子表格的最后一列，数学成绩在倒数第二列，英语成绩在倒数第三列。
nm =  ('raju','anil','ravi','amar')
dv =  ('f.y.',  's.y.',  's.y.',  'f.y.')
ind = np.lexsort((dv,nm))
print ('调用 lexsort() 函数：')
print (ind)
print ('\n')
print ('使用这个索引来获取排序后的数据：')
print ([nm[i]  +  ", "  + dv[i]  for i in ind])
# 上面传入 np.lexsort 的是一个tuple，排序时首先排 nm，顺序为：amar、anil、raju、ravi 。综上排序结果为 [3 1 0 2]。

# numpy.argmax() 和 numpy.argmin()
# numpy.argmax() 和 numpy.argmin()函数分别沿给定轴返回最大和最小元素的索引。
a = np.array([[30,40,70],[80,20,10],[50,90,60]])
print  ('我们的数组是：')
print (a)
print ('\n')
print ('调用 argmax() 函数：')
print (np.argmax(a))
print ('\n')
print ('展开数组：')
print (a.flatten())
print ('\n')
print ('沿轴 0 的最大值索引：')
maxindex = np.argmax(a, axis =  0)
print (maxindex)
print ('\n')
print ('沿轴 1 的最大值索引：')
maxindex = np.argmax(a, axis =  1)
print (maxindex)
print ('\n')
print ('调用 argmin() 函数：')
minindex = np.argmin(a)
print (minindex)
print ('\n')
print ('展开数组中的最小值：')
print (a.flatten()[minindex])
print ('\n')
print ('沿轴 0 的最小值索引：')
minindex = np.argmin(a, axis =  0)
print (minindex)
print ('\n')
print ('沿轴 1 的最小值索引：')
minindex = np.argmin(a, axis =  1)
print (minindex)

# numpy.nonzero()
# numpy.nonzero() 函数返回输入数组中非零元素的索引。
a = np.array([[30,40,0],[0,20,10],[50,0,60]])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 nonzero() 函数：')
print (np.nonzero (a))

# numpy.where()
# numpy.where() 函数返回输入数组中满足给定条件的元素的索引。
x = np.arange(9.).reshape(3,  3)
print ('我们的数组是：')
print (x)
print ( '大于 3 的元素的索引：')
y = np.where(x >  3)
print (y)
print ('使用这些索引来获取满足条件的元素：')
print (x[y])

# numpy.extract()
# numpy.extract() 函数根据某个条件从数组中抽取元素，返回满条件的元素。
x = np.arange(9.).reshape(3,  3)
print ('我们的数组是：')
print (x)
# 定义条件, 选择偶数元素
condition = np.mod(x,2)  ==  0
print ('按元素的条件值：')
print (condition)
print ('使用条件提取元素：')
print (np.extract(condition, x))






