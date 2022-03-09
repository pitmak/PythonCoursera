n, k = map(int, input().split())
lst = [1] * n
for i in range(k):
    a, b = map(int, input().split())
    for j in range(a - 1, b):
        lst[j] = 0
for elem in lst:
    print('I' if elem == 1 else '.', end='')
