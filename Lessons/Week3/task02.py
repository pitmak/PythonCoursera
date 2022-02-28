n = int(input())

res = 0
i = 1
while i <= n:
    res += 1 / i / i
    i += 1

print(res)
