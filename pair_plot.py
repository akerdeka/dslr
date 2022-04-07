import sys
import csv
from numpy import NaN

from libGraph import Graph

class PairPlot:

    def __init__(self) -> None:
        self.all_tab = {}
        self.header = []

    def convertToFloat(self):
        for i in self.all_tab.items():
            for index, element in enumerate(i[1]):
                if i[0] == 'Index':
                    break
                try:
                    if element == '':
                        self.all_tab[i[0]][index] = NaN
                    else:
                        self.all_tab[i[0]][index] = float(element)
                except:
                    continue

    def drawPairPlot(self):
        csv_arg = sys.argv[1]
        file = open(csv_arg)
        csvreader = csv.reader(file)

        for index, row in enumerate(csvreader):
            if index == 0:
                self.header = row
                for i in range(len(row)):
                    self.all_tab[row[i]] = []
            else:
                for i in range(len(row)):
                    self.all_tab[self.header[i]].append(row[i])

        PairPlot.convertToFloat(self)

        Graph.PairPlot(self.all_tab)
        

Pp = PairPlot()

Pp.drawPairPlot()