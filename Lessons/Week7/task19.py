res = {}
total = 0
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file.read().splitlines():
        if line not in res:
            res[line] = 0
        res[line] += 1
        total += 1
lst = []
for key in res:
    lst.append((res[key], key))
lst.sort(reverse=True)
with open('output.txt', 'w', encoding='utf-8') as file:
    if 2 * lst[0][0] > total:
        print(lst[0][1], file=file)
    else:
        print(lst[0][1], lst[1][1], sep='\n', file=file)
