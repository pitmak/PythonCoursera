a = int(input())
b = int(input())
c = int(input())

res = a % 2 + b % 2 + c % 2
if res == 1 or res == 2:
    print('YES')
else:
    print('NO')
