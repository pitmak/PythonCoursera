import math


def lagr(n, imax):
    if imax == 0:
        return -1
    s = int(math.sqrt(n))
    if s * s == n:
        return s,
    else:
        for i in range(s, 0, -1):
            rec = lagr(n - i * i, imax - 1)
            if rec != -1:
                return (i,) + rec
        return -1


print(*lagr(int(input()), 4))
