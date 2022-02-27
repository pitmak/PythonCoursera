n = int(input())

palCount = 0
i = 1
while i <= n:
    pal = 0
    j = i
    while j > 0:
        pal = pal * 10 + j % 10
        j //= 10
    if i == pal:
        palCount += 1
    i += 1
print(palCount)
