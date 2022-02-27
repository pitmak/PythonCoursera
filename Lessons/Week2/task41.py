n = int(input())
prev = 0
fibo = 1
i = 1
while n >= fibo:
    if n == fibo:
        print(i)
        break
    prev, fibo = fibo, prev + fibo
    i += 1
else:
    print(-1)
