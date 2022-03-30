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