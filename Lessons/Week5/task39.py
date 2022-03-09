desk = [[0] * 8 for i in range(8)]


def is_fight():
    for i in range(8):
        sum_v = sum_h = 0
        sum_d1 = sum_d2 = sum_d3 = sum_d4 = 0
        for j in range(8):
            sum_v += desk[i][j]
            sum_h += desk[j][i]
        if sum_v > 1 or sum_h > 1:
            return True
        for j in range(i + 1):
            sum_d1 += desk[i - j][j]
            sum_d2 += desk[7 - j][7 - i + j]
            sum_d3 += desk[j][7 - i + j]
            sum_d4 += desk[7 - i + j][j]
        if sum_d1 > 1 or sum_d2 > 1 or sum_d3 > 1 or sum_d4 > 1:
            return True
    return False


for i in range(8):
    x, y = map(int, input().split())
    desk[x - 1][y - 1] = 1

print('YES' if is_fight() else 'NO')
