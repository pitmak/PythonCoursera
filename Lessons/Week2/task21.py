a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0 and b == 0:
    print('INF')
elif a == 0:
    print('NO')
else:
    if b % a == 0:
        if d - c * b // a != 0:
            print(-b // a)
        else:
            print('NO')
    else:
        print('NO')
