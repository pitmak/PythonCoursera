a = set()
b = set()
with open('input.txt', 'r', encoding='utf8') as file:
    n, m = map(int, file.readline().split())
    for i in range(n):
        a.add(int(file.readline()))
    for i in range(m):
        b.add(int(file.readline()))

aib = a & b
print(len(aib))
print(*sorted(aib))
amb = a - b
print(len(amb))
print(*sorted(amb))
bma = b - a
print(len(bma))
print(*sorted(bma))
