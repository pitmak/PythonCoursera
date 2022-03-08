lst = input().split()

max = int(lst[0])
imax = 0
for i in range(1, len(lst)):
    if int(lst[i]) > max:
        max = int(lst[i])
        imax = i
print(max, imax)
