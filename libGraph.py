import math
from sys import stdin
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class Graph:

    @staticmethod
    def Histogram(datas: list):
        data = []
        for i in range(len(datas)):
            data.append([])
        for index, i in enumerate(datas):
            for element in i:
                if type(element) != str:
                    if math.isnan(element):
                        continue
                data[index].append(element)
        colors = ['red', 'blue', 'green', 'orange']
        label = ["Gryffindor", "Ravenclaw", "Slytherin","Hufflepuff"]
        for index, i in enumerate(data):
            plt.hist(i, color=colors[index], alpha=0.5, label=label[index])
        plt.legend(["Gryffindor", "Ravenclaw", "Slytherin","Hufflepuff"])
        plt.title("Care of Magical Creatures marks by house")
        plt.xlabel("Mark")
        plt.ylabel("Number of mark")
        plt.savefig("images/histogram.png")

    @staticmethod
    def ScatterPlot(data: list, color):
        plt.scatter(data[0][1:], data[1][1:], c=color, alpha=0.5)
        plt.legend(["Gryffindor", "Ravenclaw", "Slytherin","Hufflepuff"])
        plt.xlabel("Defense Against the Dark Arts")
        plt.ylabel("Astronomy")
        plt.savefig("images/scatter_plot.png")

    @staticmethod
    def PairPlot(data: dict):
        df = pd.DataFrame(data)
        sns.pairplot(df, hue = 'Hogwarts House',palette = "tab10")
        plt.savefig("images/pairplot.png")
