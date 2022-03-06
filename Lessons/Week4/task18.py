def c(n, k):
    if n == k:
        return 1
    if k == 1:
        return n
    if k == 0:
        return 1
    return c(n - 1, k) + c(n - 1, k - 1)


print(c(int(input()), int(input())))
