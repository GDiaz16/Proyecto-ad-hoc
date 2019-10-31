# exponenciacion modular
import numpy as np


def ex(base, exp, m):
    r = 1
    while (exp):
        if (exp & 1):
            r = (r * base) % m
        exp >>= 1
        base = ((base % m) * (base % m)) % m
    return r


print(ex(222222, 55252552, 29))