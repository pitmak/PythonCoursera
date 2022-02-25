a = int(input())
b = int(input())
c = int(input())

res = (a == b) + (b == c) + (c == a)
if res == 1:
    res = 2
print(res)
