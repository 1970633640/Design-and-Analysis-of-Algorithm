from random import random
from math import sqrt

k = 0
n = 1000000000
for i in range(n):
    x = random()
    y = random()
    if y <= sqrt(1 - x ** 2):
        k = k + 1
print(4 * k / n)
