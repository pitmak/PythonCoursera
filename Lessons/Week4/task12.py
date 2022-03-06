def power(a, n):
    res = 1
    for i in range(abs(n)):
        if n > 0:
            res *= a
        else:
            res /= a
    return res


a = float(input())
n = int(input())

print(power(a, n))
