lst = input().split()
for i in range(len(lst) // 2):
    lst[i], lst[-1 - i] = lst[-1 - i], lst[i]
print(*lst)
