from math import inf
from time import perf_counter
from random import randrange
import sys


class RodCutter:
    def __init__(self, inches):
        self.inches = inches
        self.price = [0] * inches
        previous = 0
        for i in range(inches):
            price = randrange(previous + 1, inches + previous, 1)
            if price == previous:
                price += 1
            self.price[i] = price
            previous = self.price[i]
        print(self.price)

    def glacier_cut_rod(self, n):
        if n == 0:
            return 0

        q = inf
        for i in range(1, n):
            q = max(q, self.price[i] + self.glacier_cut_rod(n - i))
        return q


def main():
    rc = RodCutter(50)
    for i in range(2, 40):
        start = perf_counter()
        rc.glacier_cut_rod(i)
        stop = perf_counter()
        print(f"Elapsed time in seconds for a rod of length {i} : {stop-start}")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
