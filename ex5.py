# 用上述算法，估计整数子集1~n的大小，并分析n对估计值的影响

from random import choice
import math


def SetCount(X):
    k = 0
    S = set()
    a = choice(X)
    while True:
        k = k + 1
        S.add(a)
        a = choice(X)
        if a in S:
            break
    return 2 * k * k / math.pi


n = 1
while n <= 100000:
    total = 0.0
    for t in range(100):
        X = []
        for i in range(1, n + 1):
            X.append(i)
        total += math.fabs(SetCount(X) - n) / n
    print(n, total / n)
    n = n * 5
