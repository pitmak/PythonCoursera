maxElem = 0
maxInd = 0
i = 0
for n in input().split():
    if int(n) >= maxElem:
        maxElem = int(n)
        maxInd = i
    i += 1
print(maxElem, maxInd)
