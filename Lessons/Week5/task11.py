n = int(input())
normSum = 0
factSum = 0
for i in range(1, n):
    factSum += int(input())
    normSum += i
print(normSum + n - factSum)
