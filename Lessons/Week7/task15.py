with open('input.txt', 'r', encoding='utf8') as file:
    d1 = {}
    d2 = {}
    n = int(file.readline())
    for i in range(n):
        a, b = file.readline().split()
        d1[a] = b
        d2[b] = a
    w = file.readline().strip()
    if w in d1:
        print(d1[w])
    elif w in d2:
        print(d2[w])
