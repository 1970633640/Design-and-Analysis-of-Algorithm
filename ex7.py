import random
from math import sqrt

n = 10000
val = []  # 数组
ptr = []  # 下一项指针
head = 0  # 链头
sa = []
sb = []
sc = []
sd = []

# 初始化数组 （链中指向数组编号从1开始 0表示结尾
for i in range(0, n):
    val.append(i)
random.shuffle(val)
for i in val:
    if i != n - 1:
        ptr.append(val.index(i + 1))
    else:
        ptr.append(-1)
head = val.index(0)


def search(x, i):
    count = 0
    while x > val[i]:
        i = ptr[i]
        count += 1
    return i, count


def a(x):  # o(n)
    return search(x, head)


def b(x):  # o(sqrt(n))
    i = head
    max = val[i]
    for j in range(0, int(sqrt(n))):
        y = val[j]
        if max < y <= x:
            i = j
            max = y
    return search(x, i)


def c(x):  # o(sqrt(n)) Sherwood
    i = head
    max = val[i]
    for j in range(0, int(sqrt(n))):
        jj = random.randint(0, n - 1)
        y = val[jj]
        if max < y <= x:
            i = jj
            max = y
    return search(x, i)


def d(x):  # o(n)
    count = 0
    i = random.randint(0, n - 1)
    y = val[i]
    if x < y:
        return search(x, head)
    elif x > y:
        return search(x, ptr[i])
    else:
        return i, 0


for i in range(100):
    x = random.randint(0, n - 1)
    sa.append(a(x)[1])
    sb.append(b(x)[1])
    sc.append(c(x)[1])
    sd.append(d(x)[1])
print(sum(sa) / len(sa))
print(sum(sb) / len(sb))
print(sum(sc) / len(sc))
print(sum(sd) / len(sd))
