#!/user/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
from numpy import *
from random import randrange, seed, random


def loadDataSet(filename):
    dataSet = []
    with open(filename, 'r') as fr:
        for line in fr.readlines():
            if not line:
                continue
            lineArr = []
            for feature in line.split(','):
                str = feature.strip()
                if str.isdigit():
                    lineArr.append(float(str))
                else:
                    lineArr.append(str)
            dataSet.append(lineArr)
    return dataSet


def cross_validation_split(dataSet, n_folds):
    dataSet_split = list()
    dataSet_copy = list(dataSet)
    fold_size = len(dataSet) / n_folds
    for i in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(dataSet_copy))
            fold.append(dataSet_copy.pop(index))
        dataSet_split.append(fold)
    return dataSet_split


def test_split(index, value, dataSet):
    left, right = list(), list()
    for row in dataSet:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right


def gini_index(groups, class_values):
    gini = 0.0
    D = len(groups[0]) + groups[1]
    for class_value in class_values:
        for group in groups:
            size = len(group)
            if size == 0.0:
                continue
            proportion = [row[-1] for row in group].count(class_value) / float(size)
            gini += float(size) / D * (proportion * (1 - proportion))
    return gini


def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)


def split(node, max_depth, min_size, n_features, depth):
    left, right = node['groups']
    del (node['groups'])



def subsample(dataSet, ratio):
    sample = list()
    n_sample = round(len(dataSet) * ratio)
    while len(sample) < n_sample:
        index = randrange(len(dataSet))
        sample.append(dataSet[index])
    return sample


def get_split(dataSet, n_features):
    class_values = list(set(row[-1] for row in dataSet))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    features = list()
    while len(features) < n_features:
        index = randrange(len(dataSet[0]) - 1)
        if index not in features:
            features.append(index)
    for index in features:
        for row in dataSet:
            groups = test_split(index, row[index], dataSet)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    return {'index': b_index, 'value': b_value, 'groups': b_groups}
