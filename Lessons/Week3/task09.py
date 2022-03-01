import math

count = 0
sumOne = 0
sumSqr = 0
while True:
    n = float(input())
    if n < 1e-20:
        break
    sumOne += n
    sumSqr += n * n
    count += 1

s = sumOne / count
print(math.sqrt((sumSqr - 2 * s * sumOne + count * s * s) / (count - 1)))
