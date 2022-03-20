def normal(arg):
    res = ''
    for char in arg:
        if char.isdigit():
            res += char
    if len(res) == 11:
        return res[1:]
    else:
        return '495' + res


with open('input.txt', 'r', encoding='utf8') as file:
    etalon = normal(file.readline())
    for i in range(3):
        if etalon == normal(file.readline()):
            print('YES')
        else:
            print('NO')
