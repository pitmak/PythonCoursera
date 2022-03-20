with open('input.txt', 'r', encoding='utf8') as file:
    res = {}
    for elem in file.read().split():
        if elem not in res:
            res[elem] = 0
        print(res[elem], end=' ')
        res[elem] += 1
