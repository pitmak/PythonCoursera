lst = list(map(int, input().split()))

if lst[0] <= lst[1] <= lst[2]:
    max3, max2, max1 = lst[0], lst[1], lst[2]
    min1, min2 = lst[0], lst[1]
elif lst[0] <= lst[2] <= lst[1]:
    max3, max2, max1 = lst[0], lst[2], lst[1]
    min1, min2 = lst[0], lst[2]
elif lst[1] <= lst[0] <= lst[2]:
    max3, max2, max1 = lst[1], lst[0], lst[2]
    min1, min2 = lst[1], lst[0]
elif lst[1] <= lst[2] <= lst[0]:
    max3, max2, max1 = lst[1], lst[2], lst[0]
    min1, min2 = lst[1], lst[2]
elif lst[2] <= lst[0] <= lst[1]:
    max3, max2, max1 = lst[2], lst[0], lst[1]
    min1, min2 = lst[2], lst[0]
elif lst[2] <= lst[1] <= lst[0]:
    max3, max2, max1 = lst[2], lst[1], lst[0]
    min1, min2 = lst[2], lst[1]

for i in range(3, len(lst)):
    if lst[i] >= max1:
        max3, max2, max1 = max2, max1, lst[i]
    elif lst[i] >= max2:
        max3, max2 = max2, lst[i]
    elif lst[i] > max3:
        max3 = lst[i]
    if lst[i] <= min1:
        min1, min2 = lst[i], min1
    elif lst[i] < min2:
        min2 = lst[i]

if min1 * min2 > max2 * max3 and max1 > 0:
    print(min1, min2, max1)
else:
    print(max3, max2, max1)
