def isPointInArea(x, y):
    return (y + x >= 0 and y - 2 * x >= 2 and
            (y - 1) ** 2 + (x + 1) ** 2 <= 4 or
            y + x <= 0 and y - 2 * x <= 2 and
            (y - 1) ** 2 + (x + 1) ** 2 >= 4)


print('YES' if isPointInArea(float(input()), float(input())) else 'NO')
