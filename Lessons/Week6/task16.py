school = [0] * 100
with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        n1, n2, sc, ball = line.split()
        school[int(sc)] += 1
    sc_t = []
    for i in range(len(school)):
        sc_t.append((-school[i], i))
    sc_t.sort()
    for elem in sc_t:
        if elem[0] == sc_t[0][0]:
            print(elem[1], end=' ')
        else:
            break
