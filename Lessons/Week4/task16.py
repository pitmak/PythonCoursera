def nod(a, b):
    if b == 0:
        return a
    return nod(b, a % b)


def ReduceFraction(n, m):
    d = nod(n, m)
    return n // d, m // d


print(*ReduceFraction(int(input()), int(input())))
