from numpy import NaN, character
import math
import numpy as np
import numpy
from libMachineLearning import MachineLearning
from libMath import Math, getStats

from libMachineLearning import MachineLearning as ml
import matplotlib.pyplot as plt
import sys
import csv

class Predict:

    def __init__(self) -> None:
        self.all_tab = []
        self.data_tab = []
        self.tab_normalize = []
        self.features = []
        self.feat_means = []
        self.datas = []
        self.houses = []

    def convertToFloat(self):
        #{"Gryffindor": 0.0, "Slytherin": 0.0, "Ravenclaw": 0.0, "Hufflepuff": 0.0}
        tmp_feat = []
        for i in range(len(self.all_tab)):
            tmp = []
            if i == 0:
                tmp_feat = self.all_tab[0]
            for j in range(1, len(self.all_tab[i])):
                try:
                    if self.all_tab[i][j] == 'Nan':
                        continue
                    if self.all_tab[i][j] == '':
                        self.all_tab[i][j] = NaN
                    if tmp_feat[j] == "Hogwarts House":
                        continue
                    self.all_tab[i][j] = float(self.all_tab[i][j])
                    if ((tmp_feat[j] in self.features) == False) and (tmp_feat[j] != "Hogwarts House"):
                        self.features.append(tmp_feat[j])
                    tmp.append(self.all_tab[i][j])
                except:
                    continue
            if tmp != []:
                self.data_tab.append(tmp)

    def ParseDataSet(self):
        csv_arg = sys.argv[1]
        file = open(csv_arg)
        csvreader = csv.reader(file)

        for row in csvreader:
            self.all_tab.append(row)


        Predict.convertToFloat(self)

    def Predict(self):

        numpy.set_printoptions(threshold=sys.maxsize)
        house_names = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]

        for i in self.features:
            self.feat_means.append(getStats.getMean(getStats.filter(i, self.all_tab)[1:]))
            self.tab_normalize.append(getStats.filter(i, self.all_tab)[1:])
        
        for idx, i in enumerate(self.tab_normalize):
            for index, j in enumerate(i):
                if math.isnan(j):
                    self.tab_normalize[idx][index] = float(self.feat_means[idx])

        for idx, i in enumerate(self.tab_normalize):
            self.tab_normalize[idx] = Math.normalize(i)

        for i in range(len(self.data_tab)):
            for j in range(len(self.features)):
                self.data_tab[i][j] = self.tab_normalize[j][i]
            self.datas.append([])

        X = np.array(self.data_tab)

        with open('saved_datas/Gryffindor.npy', 'rb') as f:
            W = np.load(f)
            b = np.load(f)
        A = MachineLearning.Predict(X, W, b)
        for idx, i in enumerate(A):
            self.datas[idx].append(float(i))
        
        with open('saved_datas/Slytherin.npy', 'rb') as f:
            W = np.load(f)
            b = np.load(f)
        A = MachineLearning.Predict(X, W, b)
        for idx, i in enumerate(A):
            self.datas[idx].append(float(i))

        with open('saved_datas/Ravenclaw.npy', 'rb') as f:
            W = np.load(f)
            b = np.load(f)
        A = MachineLearning.Predict(X, W, b)
        for idx, i in enumerate(A):
            self.datas[idx].append(float(i))

        with open('saved_datas/Hufflepuff.npy', 'rb') as f:
            W = np.load(f)
            b = np.load(f)
        A = MachineLearning.Predict(X, W, b)
        for idx, i in enumerate(A):
            self.datas[idx].append(float(i))

        for index, stud in enumerate(self.datas):
            tmp = 0.0
            self.houses.append("")
            for idx, mark in enumerate(stud):
                if mark > tmp:
                    tmp = mark
                    self.houses[index] = house_names[idx]
        


Tr = Predict()

Tr.ParseDataSet()
Tr.Predict()