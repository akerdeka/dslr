from numpy import empty_like
from libMath import Math

class getStats:


    @staticmethod
    def getEmptyDatas(data: list) -> int:
        empty_data = 0
        for i in data:
            if i == None:
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
                total += float(i)
        return (total / float(len(data)) - getStats.getEmptyDatas(data))

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
        return (float(data[0]))

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
