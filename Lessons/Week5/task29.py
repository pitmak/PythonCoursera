lst = list(map(int, input().split()))
x = int(input())

i = 0
for elem in lst:
    i += 1
    if x > elem:
        break
else:
    i += 1
print(i)
