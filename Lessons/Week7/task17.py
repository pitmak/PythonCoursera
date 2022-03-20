with open('input.txt', 'r', encoding='utf8') as file:
    res = {}
    for word in file.read().split():
        if word not in res:
            res[word] = 0
        res[word] += 1
    lst = []
    for key in res:
        lst.append((-res[key], key))
    lst.sort()
    print(lst[0][1])
