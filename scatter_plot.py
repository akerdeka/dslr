import sys
import csv
from numpy import NaN

from libGraph import Graph
from getStats import getStats

class ScatterPlot:

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

    def drawScatterPlot(self):
        csv_arg = sys.argv[1]
        file = open(csv_arg)
        csvreader = csv.reader(file)

        for row in csvreader:
            self.all_tab.append(row)

        ScatterPlot.convertToFloat(self)
        tab = []
        tab.append(getStats.filter("Defense Against the Dark Arts", self.all_tab, "Gryffindor"))
        tab.append(getStats.filter("Astronomy", self.all_tab, "Gryffindor"))

        Graph.ScatterPlot(tab, "r")

        tab = []
        tab.append(getStats.filter("Defense Against the Dark Arts", self.all_tab, "Ravenclaw"))
        tab.append(getStats.filter("Astronomy", self.all_tab, "Ravenclaw"))

        Graph.ScatterPlot(tab, "b")

        tab = []
        tab.append(getStats.filter("Defense Against the Dark Arts", self.all_tab, "Slytherin"))
        tab.append(getStats.filter("Astronomy", self.all_tab, "Slytherin"))

        Graph.ScatterPlot(tab, "g")

        tab = []
        tab.append(getStats.filter("Defense Against the Dark Arts", self.all_tab, "Hufflepuff"))
        tab.append(getStats.filter("Astronomy", self.all_tab, "Hufflepuff"))

        Graph.ScatterPlot(tab, "orange")

Sc = ScatterPlot()

Sc.drawScatterPlot()