lst = input().split()
k = int(input())
for i in range(k, len(lst)-1):
    lst[i] = lst[i + 1]
lst.pop()
print(*lst)
