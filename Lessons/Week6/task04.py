s = int(input()) - 3
c = 0
for n in sorted(map(int, input().split())):
    if n >= s + 3:
        c += 1
        s = n
print(c)
