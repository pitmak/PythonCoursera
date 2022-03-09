lst = list(map(int, input().split()))

n = 0
max_count = 0

for elem in lst:
    c = lst.count(elem)
    if c > max_count:
        max_count = c
        n = elem

print(n)
