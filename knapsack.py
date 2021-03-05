from math import inf
from time import perf_counter
from random import randrange
import sys


class KnapSack:
    def __init__(self, items):
        self.n = items
        self.wt = [0] * items
        self.val = [0] * items
        total_weight = 0
        for i in range(items):
            self.wt[i] = randrange(1, 100)
            self.val[i] = randrange(1, 100)
            total_weight += self.wt[i]
        self.W = int(total_weight / 2)

    def slow_thief(self):
        self._knapsack_slow(self.W, self.n)

    def _knapsack_slow(self, capacity, n):
        if n == 0 or self.W == 0:
            return 0

        if self.wt[n-1] > capacity:
            return self._knapsack_slow(capacity, n-1)
        else:
            return max(self.val[n-1] + self._knapsack_slow(capacity - self.wt[n-1], n-1),
                       self._knapsack_slow(capacity, n-1))


def main():
    for i in range(2, 100):
        thief = KnapSack(i)
        start = perf_counter()
        thief.slow_thief()
        stop = perf_counter()
        print(f"Elapsed time in seconds for a rod of length {i} : {stop-start}")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()