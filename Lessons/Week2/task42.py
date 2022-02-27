a = int(input())
b = int(input())

while a > b:
    if a % 2 == 1:
        a -= 1
        print('-1')
    else:
        if a >= b * 2:
            a //= 2
            print(':2')
        else:
            a -= 1
            print('-1')
