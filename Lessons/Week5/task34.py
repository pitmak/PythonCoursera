lst = list(map(int, input().split()))
min1 = max2 = min(lst[0], lst[1])
min2 = max1 = max(lst[0], lst[1])
for i in range(2, len(lst)):
    if lst[i] >= max1:
        max2 = max1
        max1 = lst[i]
    elif lst[i] > max2:
        max2 = lst[i]
    if lst[i] <= min1:
        min2 = min1
        min1 = lst[i]
    elif lst[i] < min2:
        min2 = lst[i]
if max1 * max2 > min1 * min2:
    print(max2, max1)
else:
    print(min1, min2)
