s, n = map(int, input().split())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()
count = 0
for elem in lst:
    if elem <= s:
        count += 1
        s -= elem
    else:
        break
print(count)
