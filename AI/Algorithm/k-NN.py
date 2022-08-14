#!/user/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
import operator


# 定义KNN算法分类器函数
# 函数参数包括: (测试数据, 训练数据, 分类, k值)
def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  # 读取矩阵有几层数据
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet  # 将测试数据转化为数值相同的行向量,再与训练集作差
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)  # axis=1 按行相加;axis=0 按列相加
    distances = sqDistances ** 0.5  # 计算欧式距离
    sortedDistIndicies = distances.argsort()  # 排序并返回index,注意此处返回的是索引而不是具体值!
    # 选择距离最近的k个值
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1  # get()相当于将其赴初值0然后加1
    # 排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True) # items()返回一个元组,operator.itemgetter()按照value排序
    return sortedClassCount[0][0] #返回标签


# 定义一个生成"训练样本集"的函数,包含特征和分类信息
def createDataSet():
    group = array([[1, 1.1], [1, 1], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def main():
    group, labels = createDataSet()
    print(classify([0, 0], group, labels, 3))


if __name__ == '__main__':
    main()
