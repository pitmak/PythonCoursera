n = int(input())
x = float(input())

res = 0
i = 0
while i <= n:
    a = float(input())
    res = res * x + a
    i += 1

print(res)
