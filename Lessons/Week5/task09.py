a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
count = 0
for x in range(1001):
    if x != e and (a * x ** 3 + b * x ** 2 + c * x + d) / (x - e) == 0:
        count += 1
print(count)
