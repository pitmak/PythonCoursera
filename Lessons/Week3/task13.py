a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
    print(5)
elif a != 0 and b != 0 and e != 0 and c / a == d / b == f / e:
    print(1, -a / b, e / b)
elif c != 0 and d != 0 and f != 0 and a / c == b / d == e / f:
    print(1, -c / d, f / d)
elif a != 0 and b != 0 and e != 0 and c / a == d / b != f / e:
    print(0)
elif c != 0 and d != 0 and f != 0 and a / c == b / d != e / f:
    print(0)
elif a == 0 and c == 0:


k = (b * c - a * d)
x = (b * f - d * e) / k
y = (c * e - a * f) / k

print(x, y)
