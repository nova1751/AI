#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
from numpy import *
from os import listdir


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):  # need to remember the range
        voteIlLabel = labels[sortedDistIndicies[i]]
        classCount[voteIlLabel] = classCount.get(voteIlLabel, 0) + 1
    maxClassCount = max(classCount, key=classCount.get)
    return maxClassCount


def test1():
    group, labels = createDataSet()
    print(str(group))
    print(str(labels))
    print(classify0([0.1, 0.1], group, labels, 3))


def file2Matrix(filename):
    fr = open(filename)
    numberOfLine = len(fr.readlines())
    returnMat = zeros((numberOfLine, 3))
    classLabelVector = []
    index = 0
    fr = open(filename)
    for line in fr.readlines():
        line = line.strip()
        listFromline = line.split('\t')
        returnMat[index, :] = listFromline[0:3]
        classLabelVector.append(int(listFromline[-1]))
        index += 1
    return returnMat, classLabelVector


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def datingClassTest():
    hoRatio = 0.1
    datingDataMat, datingLabels = file2Matrix('../Resources/datingTestSet2.txt')
    normDataSet, ranges, minVals = autoNorm(datingDataMat)
    m = normDataSet.shape[0]
    numberVec = int(m * hoRatio)
    errorCount = 0
    for i in range(numberVec):
        classLabel = classify0(normDataSet[i, :], normDataSet[numberVec:m, :], datingLabels[numberVec:m], 3)
        print('the predicted result is %d,the real result is %d ' % (classLabel, datingLabels[i]))
        if (classLabel != datingLabels[i]): errorCount += 1
    print('the total error rate is %f' % (errorCount / float(numberVec)))
    print(errorCount)


def img2filename(filename):
    returnMat = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        line = fr.readline()
        for j in range(32):
            returnMat[0, i * 32 + j] = int(line[j])
    return returnMat


def handWritingTest():
    hwlabels = []
    trainingFileList = listdir('../Resources/trainingDigits')
    m = len(trainingFileList)
    trainingDataSet = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        fileNumStr = int(fileStr.split('_')[0])
        hwlabels.append(fileNumStr)
        trainingDataSet[i, :] = img2filename('../Resources/trainingDigits/%s' % fileNameStr)

    testFileList = listdir('../Resources/testDigits')
    mTest = len(testFileList)
    testDataSet = zeros((mTest, 1024))
    errorCount = 0.0
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        fileNumStr = int(fileStr.split('_')[0])
        testDataSet[i, :] = img2filename('../Resources/testDigits/%s' % fileNameStr)
        classLabel = classify0(testDataSet[i, :], trainingDataSet, hwlabels, 3)
        print('the predicted label is %d , the real label is %d' % (classLabel, fileNumStr))
        if (classLabel != fileNumStr): errorCount += 1
    print('the rate is %f'%(errorCount/float(mTest)))
    print(errorCount)


if __name__ == '__main__':
    # test1()
    # datingClassTest()
    handWritingTest()
