from math import sqrt

a = float(input())
b = float(input())
c = float(input())

nil = 1e-30

if a == 0:
    if b == 0:
        if c == 0:
            print(3)
        else:
            print(0)
    else:
        print(1, -c / b)
else:
    d = b * b - 4 * a * c
    if d > nil:
        x1 = (-b - sqrt(d)) / 2 / a
        x2 = (-b + sqrt(d)) / 2 / a
        if x1 > x2:
            x1, x2 = x2, x1
        print(2, x1, x2)
    elif d > -nil:
        print(1, -b / 2 / a)
    else:
        print(0)
