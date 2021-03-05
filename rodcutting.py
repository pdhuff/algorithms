from math import inf
from time import perf_counter
from random import randrange
import sys


class RodCutter:
    def __init__(self, inches):
        self.rod = [0] * inches
        self.inches = inches
        self.price = [0] * inches
        self.split = [0] * inches
        previous = 0
        for i in range(inches):
            price = randrange(previous + 1, inches + previous, 1)
            if price == previous:
                price += 1
            self.price[i] = price
            previous = self.price[i]
        print(self.price)

    def cut_rod_glacier_speed(self, n):
        if n == 0:
            return 0

        q = -inf
        for i in range(1, n):
            q = max(q, self.price[i] + self.cut_rod_glacier_speed(n - i))
        return q

    def cut_rod_walking_speed(self, n):
        if self.rod[n] >= 0:
            return self.rod[n]
        if n == 0:
            return 0

        for j in range(1, n):
            q = -inf
            for i in range(1, j):
                q_save = q
                if q < self.price[i] + self.cut_rod_walking_speed(n - i):
                    q = self.price[i] + self.cut_rod_walking_speed(n - i)
                    self.split[j] = i
            # Memo-ization step
            self.rod[n] = q
        return q

    def print_rod_cuts(self):
        #TODO: Fix the rod cuts

def main():
    rc = RodCutter(1000)
    for i in range(2, 1000):
        start = perf_counter()
        rc.cut_rod_walking_speed(i)
        stop = perf_counter()
        print(f"Elapsed time in seconds for a rod of length {i} : {stop-start}")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
