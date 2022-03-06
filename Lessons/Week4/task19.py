def getSum():
    n = int(input())
    if n == 0:
        return 0
    return n + getSum()


print(getSum())
