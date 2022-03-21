tree = {}


def get_deep(elem):
    if tree[elem] == '':
        return 0
    else:
        return 1 + get_deep(tree[elem])


with open('input.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    for line in file:
        child, parent = line.split()
        tree[child] = parent
        if parent not in tree:
            tree[parent] = ''
    for elem in sorted(tree):
        print(elem, get_deep(elem))
