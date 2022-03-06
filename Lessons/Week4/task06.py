def isPointInCircle(x, y, xc, yc, r):
    return abs((xc - x) ** 2 + (yc - y) ** 2) <= r * r


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())

print('YES' if isPointInCircle(x, y, xc, yc, r) else 'NO')
