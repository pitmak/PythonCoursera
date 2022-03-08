a = int(input())
b = int(input())
c = 1 if a < b else -1
print(*range(a, b + c, c))
