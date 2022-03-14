n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))

for i in p:
    c[i - 1] -= 1

for elem in c:
    print('YES' if elem < 0 else 'NO')
