from math import sqrt

a = float(input())
b = float(input())
c = float(input())

nil = 1e-30
d = b * b - 4 * a * c

if d > nil:
    x1 = (-b - sqrt(d)) / 2 / a
    x2 = (-b + sqrt(d)) / 2 / a
    if x1 > x2:
        x1, x2 = x2, x1
    print(x1, x2)
elif d > -nil:
    print(-b / 2 / a)
