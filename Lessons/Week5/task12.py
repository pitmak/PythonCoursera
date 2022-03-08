a = int(input())
b = int(input())
if a > b:
    a, b = b, a
for i in range(a, b + 1):
    if i // 1000 == i % 10 and i // 100 % 10 == i // 10 % 10:
        print(i)
