with open('input.txt', 'r', encoding='utf8') as file:
    pool = {}
    total = 0
    file.readline()
    for line in file:
        if line == 'VOTES:\n':
            break
        pool[line.strip()] = 0
    for line in file:
        pool[line.strip()] += 1
        total += 1
    for elem in pool:
        if pool[elem] / total >= 0.07:
            print(elem)
