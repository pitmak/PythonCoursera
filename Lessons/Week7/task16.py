with open('input.txt', 'r', encoding='utf8') as file:
    res = {}
    for line in file:
        name, count = line.split()
        if name not in res:
            res[name] = 0
        res[name] += int(count)
    for key in sorted(res):
        print(key, res[key])
