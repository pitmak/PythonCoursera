max1 = int(input())
if max1 == 0:
    max2 = 0
else:
    max2 = int(input())

if max2 > max1:
    max1, max2 = max2, max1

while max2 != 0:
    n = int(input())
    if n == 0:
        break
    if n >= max1:
        max2 = max1
        max1 = n
    elif n >= max2:
        max2 = n

print(max2)
