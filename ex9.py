# 米勒罗宾素性测试与确定性算法相比较，并给出100~10000以内错误的比例。
from math import sqrt, log10
from random import randint

def Btest(a, n):
    s = 0
    t = n - 1
    while t % 2 == 0:
        s = s + 1
        t = t // 2
    x = a ** t % n
    if x == 1 or x == n - 1:
        return True
    for i in range(1, s):
        x = x ** 2 % n
        if x == n - 1:
            return True
    return False


def MillRab(n):
    a = randint(2, n - 2)
    return Btest(a, n)


def RepeatMillRab(n):
    times = int(log10(n))
    for i in range(times):
        if MillRab(n) == False:
            return False
    return True


def getans():
    for i in range(100, 10001):
        prime = True
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            ans.add(i)


def getx():
    n = 5
    while True:
        if 100 <= n <= 10000 and RepeatMillRab(n):
            x.add(n)
        n = n + 2
        if n >= 10000:
            break

for i in range(10):
    print(i+1)
    ans = set()
    x = set()
    getans()
    getx()

    print("[100,10000]素数个数：", len(ans))
    print("米勒罗宾测试[100,10000]素数个数", len(x))
    print("米勒罗宾多出来的素数个数", len(ans.union(x).difference(ans)))
    print("米勒罗宾少了的素数个数", len(ans.union(x).difference(x)))
