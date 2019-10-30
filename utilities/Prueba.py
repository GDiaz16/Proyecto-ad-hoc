# coding: utf-8
# Your code here!
import numpy as np

A = np.matrix('26 -10;-7 21')
A = (A * 8) % 27
print(A)

B = np.matrix('10;14')
P = [[6, 4], [17, 25], [7, 9], [15, 4], [4, 8], [6, 4], [19, 14], [0, 12], [5, 17], [6, 7], [14, 14], [6, 22],
     [26, 14], [13, 13], [21, 7], [6, 7], [8, 22], [24, 0], [13, 5], [6, 4], [2, 17], [14, 5], [24, 9], [10, 22]]

D = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
     'W', 'X', 'Y', 'Z']

for i in P:
    print(D[(((np.dot(A, i) - np.dot(A, B)) % 27)[0, 0])], D[(((np.dot(A, i) - np.dot(A, B)) % 27)[1, 0])], end="  ")

##-------------------------------------------------------------------------------------------------------------##
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


print(ex(2743, 21, 2897))