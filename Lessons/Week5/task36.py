lst = list(map(int, input().split()))
count = 0
for i in range(len(lst)):
    for j in range(i):
        if lst[i] == lst[j]:
            count += 1
print(count)
