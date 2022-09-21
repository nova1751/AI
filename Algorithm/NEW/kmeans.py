#!/user/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from numpy import *


def loadDataSet(filename):
    dataSet = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)
        dataSet.append(fltLine)
    return dataSet


def calcEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))


def ranCent(dataMat, k):
    n = dataMat.shape[1]
    centroids = mat(zeros(n, k))
    for j in range(n):
        minJ = min(dataMat[:, j])
        rangeJ = float(max(dataMat[:, j]) - minJ)
        centroids[:,j] - mat(minJ+rangeJ*random.rand(k,1))
    return centroids

