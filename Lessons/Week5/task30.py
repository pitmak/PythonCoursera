lst = list(map(int, input().split()))
count = 1
for i in range(1, len(lst)):
    if lst[i] != lst[i - 1]:
        count += 1
print(count)
