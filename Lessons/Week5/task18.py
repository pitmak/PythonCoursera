def isAscending(a):
    for i in range(1, len(a)):
        if a[i] <= a[i - 1]:
            return False
    return True


print('YES' if isAscending(input().split()) else 'NO')
