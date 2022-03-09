lst = input().split()
k, c = input().split()
k = int(k)
lst.append(lst[-1])
for i in range(len(lst) - 1, k, -1):
    lst[i] = lst[i - 1]
lst[k] = c
print(*lst)
