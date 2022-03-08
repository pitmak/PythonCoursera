lst = list(map(int, input().split()))
min = 0
first = True
for n in lst:
    if n % 2 != 0:
        if first:
            min = n
            first = False
        else:
            if n < min:
                min = n
print(min)
