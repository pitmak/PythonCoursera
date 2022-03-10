def intersection(a, b):
    res = []
    i_a = 0
    i_b = 0

    while i_a < len(a) and i_b < len(b):
        if a[i_a] < b[i_b]:
            i_a += 1
        elif a[i_a] > b[i_b]:
            i_b += 1
        else:
            res.append(a[i_a])
            i_a += 1
            i_b += 1

    return res


print(*intersection(list(map(int, input().split())),
                    list(map(int, input().split()))))
