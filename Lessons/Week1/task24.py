a = int(input())
b = int(input())
res = 0 ** (a % b)
print('YES' * res, 'NO' * (1 - res), sep='')
