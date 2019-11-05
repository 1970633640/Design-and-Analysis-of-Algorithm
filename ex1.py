from random import random

k = 0
n = 10000000
for i in range(n):
    x = random()
    y = x
    if x ** 2 + y ** 2 <= 1:
        k = k + 1
print(4 * k / n)
