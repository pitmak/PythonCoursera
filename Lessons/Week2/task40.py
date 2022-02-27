n = int(input())

if n < 2:
    print(n)
else:
    prev = 0
    fibo = 1
    while n > 1:
        prev, fibo = fibo, prev + fibo
        n -= 1
    print(fibo)
