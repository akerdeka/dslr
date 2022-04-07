import csv
import sys
import pandas as pd

from libMath import getStats

class Describe:

    def __init__(self) -> None:
        self.empty_data = 0
        self.data = {}
        self.header = []
        self.features = {}
        self.stats = {'Count': 0, 'Mean': 0, 'Std': 0, 'Min': 0, '25%': 0, '50%': 0, '75%': 0, 'Max' : 0}

    def parseFile(self):
        csv_arg = sys.argv[1]
        file = open(csv_arg)
        csvreader = csv.reader(file)

        for index, row in enumerate(csvreader):
            if index == 0:
                self.header = row
                for i in range(len(row)):
                    self.data[row[i]] = []
            else:
                for i in range(len(row)):
                    self.data[self.header[i]].append(row[i])

    def getFeatures(self):
        for index, datas in enumerate(self.data.items()):
            if index != 0:
                try:
                    datas[1][0] = float(datas[1][0])
                    for i in range(1, len(datas[1])):
                        if datas[1][i] == '':
                            datas[1][i] = None
                        if datas[1][i] != None:
                            datas[1][i] = float(datas[1][i])
                except:
                    pass
                if type(datas[1][0]) == float:
                    self.features[self.header[index]] = self.stats
        for feature in self.features:
            self.features[feature] = getStats.getAllStats(self.data[feature])
    
    def printFeatures(self):

        count, mean, std, min, q1, q2, q3, max = [], [], [], [], [], [], [], []
        feature_keys = list(self.features.keys())


        for feature in self.features.items():
            count.append(feature[1]['Count'])
            mean.append(feature[1]['Mean'])
            std.append(feature[1]['Std'])
            min.append(feature[1]['Min'])
            q1.append(feature[1]['25%'])
            q2.append(feature[1]['50%'])
            q3.append(feature[1]['75%'])
            max.append(feature[1]['Max'])
        
        print("     ", end='')
        for feature in self.features.items():
            print('%*s' % (len(feature[0]) + 5, feature[0]), end='')
        print("\nCount", end='')
        for i in range(len(self.features)):
            print('%*s' % (len(feature_keys[i]) + 5, count[i]), end='')
        print("\nMean ", end='')
        for i in range(len(self.features)):
            print('%*s' % (len(feature_keys[i]) + 5, float(mean[i]).__round__(3)), end='')
        print("\nStd  ", end='')
        for i in range(len(self.features)):
            print('%*s' % (len(feature_keys[i]) + 5, float(std[i]).__round__(3)), end='')
        print("\nMin  ", end='')
        for i in range(len(self.features)):
            print('%*s' % (len(feature_keys[i]) + 5, float(min[i]).__round__(3)), end='')
        print("\n25%  ", end='')
        for i in range(len(self.features)):
            print('%*s' % (len(feature_keys[i]) + 5, float(q1[i]).__round__(3)), end='')
        print("\n50%  ", end='')
        for i in range(len(self.features)):
            print('%*s' % (len(feature_keys[i]) + 5, float(q2[i]).__round__(3)), end='')
        print("\n75%  ", end='')
        for i in range(len(self.features)):
            print('%*s' % (len(feature_keys[i]) + 5, float(q3[i]).__round__(3)), end='')
        print("\nMax  ", end='')
        for i in range(len(self.features)):
            print('%*s' % (len(feature_keys[i]) + 5, float(max[i]).__round__(3)), end='')

DSLR = Describe()

DSLR.parseFile()
DSLR.getFeatures()
DSLR.printFeatures()