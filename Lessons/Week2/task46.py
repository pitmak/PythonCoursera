prev = int(input())

prevState = 0
chainLen = 1
maxChainLen = 1

while True:
    n = int(input())
    if n == 0:
        break
    if n == prev:
        prevState = 0
        chainLen = 1
    elif (n < prev and prevState == -1) or (n > prev and prevState == 1):
        chainLen += 1
    elif n < prev:
        prevState = -1
        chainLen = 2
    elif n > prev:
        prevState = 1
        chainLen = 2
    if chainLen > maxChainLen:
        maxChainLen = chainLen
    prev = n

print(maxChainLen)
