#!/user/bin/env python3
# -*- coding: utf-8 -*-
from numpy import *
from math import log

def loadDataSet():
    """
    创建数据集
    :return: 单词列表postingList, 所属类别classVec
    """
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],  # [0,0,1,1,1......]
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec


def createVocabList(dataSet):
    vocabList = set([])
    for document in dataSet:
        vocabList = vocabList | set(document)
    return list(vocabList)


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print('the word: %s is not in my vocubulary!' % word)
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = sum(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0num = ones((1, numWords))
    p1num = ones((1, numWords))
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1num / p1Denom)
    p0Vect = log(p0num / p0Denom)
    return p0Vect, p1Vect, pAbusive

def _trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = sum(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    p0num = zeros((1, numWords))
    p1num = zeros((1, numWords))
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1num / p1Denom
    p0Vect = p0num / p0Denom
    return p0Vect, p1Vect, pAbusive
