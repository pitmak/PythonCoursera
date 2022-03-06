def isPointInSquare(x, y):
    return -1 <= abs(x) + abs(y) <= 1


print('YES' if isPointInSquare(float(input()), float(input())) else 'NO')
