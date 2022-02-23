n = int(input())
print(n % 100 - n // 1000 - n // 100 % 10 * 10 + 1)
