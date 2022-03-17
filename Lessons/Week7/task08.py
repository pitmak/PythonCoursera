with open('input.txt', 'r', encoding='utf8') as file:
    n = int(file.readline())
    possible = set(range(1, n + 1))
    while True:
        line = file.readline().strip()
        if line == 'HELP':
            break
        ann_try = set(map(int, line.split()))
        mult = possible & ann_try
        if 2 * len(mult) > len(possible):
            print('YES')
            possible = mult
        else:
            print('NO')
            possible -= ann_try
    print(*sorted(possible))
