# 写一算法，求n=12~20时最优的StepVegas值
from random import randint
import time



def queensLV(stepVegas, x, n):
    col = set()
    diag45 = set()
    diag135 = set()
    k = 0
    while True:
        nb = 0
        j = 0
        for i in range(n):
            if (i not in col) and (i - k not in diag45) and (i + k not in diag135):
                nb += 1
                if randint(1, nb) == 1:
                    j = i
        if nb > 0:
            x[k] = j
            col.add(j)
            diag45.add(j - k)
            diag135.add(j + k)
            k += 1
        if nb == 0 or k == stepVegas:
            if nb > 0:
                return backtrace(k, x, n)
            else:
                return False


def test(k, x):
    for i in range(0, k):
        if x[i] == x[k] or abs(x[k] - x[i]) == abs(k - i):
            return False
    return True


def test2(x, n):  # 彻底检查是否符合规则
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if x[i] == x[j] or abs(x[j] - x[i]) == abs(j - i):
                print(i, j, x[i], x[j])
                return False
    return True


def backtrace(start, x, n):
    if start >= n:
        return True
    for i in range(0, n):
        x[start] = i
        if test(start, x):
            if backtrace(start + 1, x, n):
                return True
    return False


print("stepVegas\tacc(times)\ttime(ms)")
for n in range(12, 21):
    #print("n=", n)
    for stepVegas in range(1, n + 1):
        total = 0
        suc = 0
        t1 = time.time()
        for _ in range(100):
            x = [-1 for _ in range(n)]
            if queensLV(stepVegas, x, n):
                suc += 1
                # if not test2(x, n):  #验算
                #     print("ERROR", x)
            total += 1
        t2 = time.time()
        #print("%d\t%d\t%.2f" % (stepVegas, suc, 1000 * (t2 - t1)))
        print("%d\t%d\t%d\t%.2f" % (n,stepVegas, suc, 1000 * (t2 - t1)))
