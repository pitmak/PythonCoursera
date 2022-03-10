n = list(map(int, input().split()))
m = list(map(int, input().split()))

res = []
i_n = 0
i_m = 0

while i_n < len(n) and i_m < len(m):
    if n[i_n] < m[i_m]:
        res.append(n[i_n])
        i_n += 1
    else:
        res.append(m[i_m])
        i_m += 1

if i_n == len(n):
    res.extend(m[i_m:])
else:
    res.extend(n[i_n:])

print(*res)
