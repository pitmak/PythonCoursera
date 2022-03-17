a, b, c, d = map(int, input().split())
set1 = set(range(min(a, b), max(a, b) + 1))
set2 = set(range(min(c, d), max(c, d) + 1))
print(len(set1 & set2))
