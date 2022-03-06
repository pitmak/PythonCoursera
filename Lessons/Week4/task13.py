def sum(a, b):
    if a > 0:
        return sum(a - 1, b + 1)
    else:
        return b


print(sum(int(input()), int(input())))
