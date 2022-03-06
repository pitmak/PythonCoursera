import math


def minDivisor(n):
    bound = int(math.sqrt(n))
    for i in range(2, bound + 1):
        if n % i == 0:
            return i
    return n


print(minDivisor(int(input())))
