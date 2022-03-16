with open('input.txt', 'r', encoding='utf8') as file:
    pool = {}
    file.readline()
    for line in file:
        if line == 'VOTES:\n':
            break
        pool[line.strip()] = 0
    for line in file:
        pool[line.strip()] += 1
    lst = []
    for elem in pool:
        lst.append((-pool[elem], elem))
    lst.sort()
    for elem in lst:
        print(elem[1])
