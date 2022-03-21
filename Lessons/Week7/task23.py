def get_accent_pos(buf):
    res = -1
    count = 0
    for i in range(len(buf)):
        if buf[i].isupper():
            res = i
            count += 1
    if count == 1:
        return res
    return -1


dic = {}

with open('input.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    for i in range(n):
        line = file.readline().strip()
        pos = get_accent_pos(line)
        if line.lower() not in dic:
            dic[line.lower()] = []
        dic[line.lower()].append(pos)

    err_count = 0
    for word in file.readline().split():
        pos = get_accent_pos(word)
        if pos == -1:
            err_count += 1
        elif word.lower() in dic and pos not in dic[word.lower()]:
            err_count += 1

    print(err_count)
