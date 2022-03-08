prev = 999999999999999
for n in input().split():
    if int(n) > prev:
        print(n, end=' ')
    prev = int(n)
