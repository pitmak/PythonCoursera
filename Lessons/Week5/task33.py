lst = list(map(int, input().split()))
min = lst[0]
imin = 0
max = lst[0]
imax = 0
for i in range(1, len(lst)):
    if lst[i] < min:
        min = lst[i]
        imin = i
    if lst[i] > max:
        max = lst[i]
        imax = i
lst[imin], lst[imax] = lst[imax], lst[imin]
print(*lst)
