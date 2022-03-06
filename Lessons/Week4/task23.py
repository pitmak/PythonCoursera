def lagr(n, imax):
    if imax == 0:
        return -1
    s = int(n ** (1 / 3))
    if s * s * s == n:
        return n,
    else:
        for i in range(s, 0, -1):
            rec = lagr(n - i * i * i, imax - 1)
            if rec != -1:
                return (i * i * i,) + rec
        return -1


res = lagr(int(input()), 7)

if res != -1:
    print(*res)
else:
    print(0)
# print(*res if res != -1 else 0)
