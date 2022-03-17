with open('input.txt', 'r', encoding='utf8') as file:
    n = int(file.readline())
    possible = set(range(1, n + 1))
    while True:
        line = file.readline().strip()
        if line == 'HELP':
            break
        if file.readline().strip() == 'YES':
            possible &= set(map(int, line.split()))
        else:
            possible -= set(map(int, line.split()))
    print(*sorted(possible))
