def isPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


print('YES' if isPointInSquare(float(input()), float(input())) else 'NO')
