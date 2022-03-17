with open('input.txt', 'r', encoding='utf8') as file:
    summ = set()
    mult = set()
    first_iter = True
    n = int(file.readline())
    for i in range(n):
        m = int(file.readline())
        curr = set()
        for j in range(m):
            curr.add(file.readline().strip())
        summ |= curr
        if first_iter:
            mult = curr
            first_iter = False
        else:
            mult &= curr
    print(len(mult))
    print(*mult, sep='\n')
    print(len(summ))
    print(*summ, sep='\n')
