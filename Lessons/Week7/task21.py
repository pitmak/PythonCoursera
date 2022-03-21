res = {}
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, good, count = line.split()
        if name not in res:
            res[name] = {}
        if good not in res[name]:
            res[name][good] = 0
        res[name][good] += int(count)
for name in sorted(res):
    print(name + ':')
    for good in sorted(res[name]):
        print(good, res[name][good])
