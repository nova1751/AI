from numpy import *


def loadDataSet(filename):
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        line = line.strip().split('\t')
        dataMat.append([float(line[0]), float(line[1])])
        labelMat.append(float(line[-1]))
    return dataMat, labelMat


def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    m, n = dataMatrix.shape
    b = 0.0
    alpha = mat(zeros((m, 1)))
    iter = 0
    while (iter < maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(multiply(alpha, labelMat).T * (dataMatrix * dataMatIn[i, :].T)) + b
            Ei=fXi-float(labelMat[i])

