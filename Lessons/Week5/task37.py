lst = list(map(int, input().split()))
for elem in lst:
    if lst.count(elem) == 1:
        print(elem, end=' ')
