n = int(input())

if 10 < n < 20:
    print(n, 'korov')
elif n % 10 == 1:
    print(n, 'korova')
elif 2 <= n % 10 <= 4:
    print(n, 'korovy')
else:
    print(n, 'korov')
