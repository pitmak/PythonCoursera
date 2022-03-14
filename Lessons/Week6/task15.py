with open('input.txt', 'r', encoding='utf8') as file:
    k = int(file.readline())
    lst = []
    for line in file:
        s = line.split()
        s1, s2, s3 = int(s[-1]), int(s[-2]), int(s[-3])
        if s1 >= 40 and s2 >= 40 and s3 >= 40:
            lst.append(s1 + s2 + s3)
    lst.sort(reverse=True)
    if k >= len(lst):
        print(0)
    elif lst[0] == lst[k]:
        print(1)
    elif lst[k] != lst[k - 1]:
        print(lst[k - 1])
    else:
        for i in range(k - 1, -1, -1):
            if lst[i] != lst[k]:
                print(lst[i])
                break
