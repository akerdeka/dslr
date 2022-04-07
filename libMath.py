import math
from numpy import NaN


class Math:

    @staticmethod
    def sqrt(nb: int):
        i = 1
        if nb < 0:
            i = -1
            nb *= i
        nb = nb**0.5
        return nb * i

    @staticmethod
    def absoluteValue(nb: int):
        if nb < 0:
            nb *= -1
        return nb

    @staticmethod
    def normalize(data: list):
        max = getStats.getMax(data)
        min = getStats.getMin(data)
        for idx, i in enumerate(data):
            data[idx] = (i - min) / (max - min)
        return data

class getStats:
    
    @staticmethod
    def swapPositions(list, pos1, pos2):
        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list

    @staticmethod
    def filter(collumn, data: list, filter = 0):
        tab = []
        collumn_idx = 0
        for index, i in enumerate(data[0]):
            if i == collumn:
                collumn_idx = index
            if index == len(data[0]) and collumn_idx == 0:
                print("Wrong filter ! Quitting...")
                exit(1)
        for element in data:
            if filter != 0:
                if filter in element:
                    tab.append(element[collumn_idx])
            else:
                tab.append(element[collumn_idx])
        return (tab)

    @staticmethod
    def getEmptyDatas(data: list) -> int:
        empty_data = 0
        for i in data:
            if (i == None) or (str(i) == "nan"):
                empty_data += 1
        return (float(empty_data))


    @staticmethod
    def getList(data: list) -> list:
        tab = []
        for i in data:
            try:
                tab.append(float(i))
            except :
                continue
        return (tab)

    @staticmethod
    def getCount(data: list) -> float:
        return (float(len(data)) - getStats.getEmptyDatas(data))

    @staticmethod
    def getMean(data: list) -> float:
        total = 0
        for i in data:
            if type(i) == float:
                if math.isnan(i):
                    total += 0
                else:
                    total += float(i)
        return (total / (float(len(data)) - getStats.getEmptyDatas(data)))

    @staticmethod
    def getStd(data: list) -> float:
        sum = 0
        mean = getStats.getMean(data)
        for i in range(len(data)):
            if type(data[i]) == float:
                sum += Math.absoluteValue(data[i] - mean)**2
        sum /= len(data)
        sum = Math.sqrt(sum)
        return (float(sum))

    @staticmethod
    def getMin(data: list) -> float:
        data = getStats.getList(data)
        data = sorted(data)
        return float(data[0])

    @staticmethod
    def getQ1(data: list) -> float:
        data = getStats.getList(data)
        data = sorted(data)
        index = (0.25 * float(len(data)) - getStats.getEmptyDatas(data)).__round__()
        return (float(data[index]))

    @staticmethod
    def getQ2(data: list) -> float:
        data = getStats.getList(data)
        data = sorted(data)
        index = (0.50 * float(len(data)) - getStats.getEmptyDatas(data)).__round__()
        return (float(data[index]))

    @staticmethod
    def getQ3(data: list) -> float:
        data = getStats.getList(data)
        data = sorted(data)
        index = (0.75 * float(len(data)) - getStats.getEmptyDatas(data)).__round__()
        return (float(data[index]))

    @staticmethod
    def getMax(data: list) -> float:
        data = getStats.getList(data)
        data = sorted(data, reverse=True)
        return (float(data[0]))

    @staticmethod
    def getAllStats(data: list) -> dict:
        dic = {
            'Count': getStats.getCount(data),
            'Mean': getStats.getMean(data),
            'Std': getStats.getStd(data),
            'Min': getStats.getMin(data),
            '25%': getStats.getQ1(data),
            '50%': getStats.getQ2(data),
            '75%': getStats.getQ3(data),
            'Max' : getStats.getMax(data)
        }
        return (dic)