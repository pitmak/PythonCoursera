n = int(input())
lst = list(map(int, input().split()))
x = int(input())

diff = 2002
res = 0
for elem in lst:
    if abs(elem - x) < diff:
        diff = abs(elem - x)
        res = elem
print(res)
