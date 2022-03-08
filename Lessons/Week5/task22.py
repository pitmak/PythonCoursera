lst = list(map(int, input().split()))
min = 1001
for n in lst:
    if 0 < n < min:
        min = n
print(min)
