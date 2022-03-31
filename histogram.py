import sys
import csv

from numpy import NaN

from libGraph import Graph
from getStats import getStats

class Histogram:

    def __init__(self) -> None:
        self.all_tab = []

    def convertToFloat(self):
        for i in range(len(self.all_tab)):
            for j in range(len(self.all_tab[i])):
                try:
                    if self.all_tab[i][j] == '':
                        self.all_tab[i][j] = NaN
                    self.all_tab[i][j] = float(self.all_tab[i][j])
                except:
                    continue

    def drawHistogram(self):
        csv_arg = sys.argv[1]
        file = open(csv_arg)
        csvreader = csv.reader(file)

        for row in csvreader:
            self.all_tab.append(row)

        Histogram.convertToFloat(self)
        tab = []
        tab.append(getStats.filter("Care of Magical Creatures", self.all_tab, "Gryffindor"))
        tab.append(getStats.filter("Care of Magical Creatures", self.all_tab, "Ravenclaw"))
        tab.append(getStats.filter("Care of Magical Creatures", self.all_tab, "Slytherin"))
        tab.append(getStats.filter("Care of Magical Creatures", self.all_tab, "Hufflepuff"))

        Graph.Histogram(tab)

Hist = Histogram()

Hist.drawHistogram()