from numpy import NaN, character
import math
import numpy as np
import numpy
from libMath import Math, getStats

from libMachineLearning import MachineLearning as ml
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import sys
import csv

class Train:

    def __init__(self) -> None:
        self.all_tab = []
        self.data_tab = []
        self.tab_normalize = []
        self.features = []
        self.feat_means = []
        self.datas = []
        self.houses = []
        self.names = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]

    def convertToFloat(self):
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
                    self.all_tab[i][j] = float(self.all_tab[i][j])
                    if (tmp_feat[j] in self.features) == False:
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


        Train.convertToFloat(self)

    def CreateCSVFile(self):
        f = open("houses.csv", 'w')
        writer = csv.writer(f)
        writer.writerow(["Index", "Hogwarts House"])
        for idx, i in enumerate(self.houses):
            tmp_row = [idx, str(self.names[i])]
            writer.writerow(tmp_row)
        f.close()

    def Train(self):

        numpy.set_printoptions(threshold=sys.maxsize)
        Gryffindor_y = []
        Ravenclaw_y = []
        Slytherin_y = []
        Hufflepuff_y = []
        check_accu = []
        house_names = [0, 1, 2, 3]

        for i in getStats.filter("Hogwarts House", self.all_tab)[1:]:
            if i == "Gryffindor":
                Gryffindor_y.append(1)
                Ravenclaw_y.append(0)
                Slytherin_y.append(0)
                Hufflepuff_y.append(0)
                check_accu.append(0)
            elif i == "Slytherin":
                Gryffindor_y.append(0)
                Ravenclaw_y.append(0)
                Slytherin_y.append(1)
                Hufflepuff_y.append(0)
                check_accu.append(1)
            elif i == "Ravenclaw":
                Gryffindor_y.append(0)
                Ravenclaw_y.append(1)
                Slytherin_y.append(0)
                Hufflepuff_y.append(0)
                check_accu.append(2)
            elif i == "Hufflepuff":
                Gryffindor_y.append(0)
                Ravenclaw_y.append(0)
                Slytherin_y.append(0)
                Hufflepuff_y.append(1)
                check_accu.append(3)

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
            #self.data_tab[i] = getStats.swapPositions(self.data_tab[i], 0, 8)

        X = np.array(self.data_tab)


        y = np.array(Gryffindor_y)
        y = y.reshape((y.shape[0], 1))
        (WG, bG) = ml.Artificial_neuron(X, y)
        A = ml.Predict(X, WG, bG)
        for idx, i in enumerate(A):
            self.datas[idx].append(float(i))
        with open('saved_datas/Gryffindor.npy', 'wb') as f:
            np.save(f, WG, allow_pickle=True)
            np.save(f, bG, allow_pickle=True)

        y = np.array(Slytherin_y)
        y = y.reshape((y.shape[0], 1))
        (WG, bG) = ml.Artificial_neuron(X, y)
        A = ml.Predict(X, WG, bG)
        for idx, i in enumerate(A):
            self.datas[idx].append(float(i))
        with open('saved_datas/Slytherin.npy', 'wb') as f:
            np.save(f, WG, allow_pickle=True)
            np.save(f, bG, allow_pickle=True)
        
        y = np.array(Ravenclaw_y)
        y = y.reshape((y.shape[0], 1))
        (WG, bG) = ml.Artificial_neuron(X, y)
        A = ml.Predict(X, WG, bG)
        for idx, i in enumerate(A):
            self.datas[idx].append(float(i))
        with open('saved_datas/Ravenclaw.npy', 'wb') as f:
            np.save(f, WG, allow_pickle=True)
            np.save(f, bG, allow_pickle=True)

        y = np.array(Hufflepuff_y)
        y = y.reshape((y.shape[0], 1))
        (WG, bG) = ml.Artificial_neuron(X, y)
        A = ml.Predict(X, WG, bG)
        for idx, i in enumerate(A):
            self.datas[idx].append(float(i))
        with open('saved_datas/Hufflepuff.npy', 'wb') as f:
            np.save(f, WG, allow_pickle=True)
            np.save(f, bG, allow_pickle=True)

        for index, stud in enumerate(self.datas):
            tmp = 0.0
            self.houses.append(0)
            for idx, mark in enumerate(stud):
                if mark > tmp:
                    tmp = mark
                    self.houses[index] = house_names[idx]

        print("Total score: ", accuracy_score(check_accu, self.houses) * 100, "%")

Tr = Train()

Tr.ParseDataSet()
Tr.Train()
Tr.CreateCSVFile()