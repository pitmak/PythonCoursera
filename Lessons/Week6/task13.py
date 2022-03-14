with open('input.txt', 'r', encoding='utf8') as file:
    file.readline()
    lst = []
    for line in file:
        name, ball = line.split()
        lst.append((-int(ball), name))
    for elem in sorted(lst):
        print(elem[1])
