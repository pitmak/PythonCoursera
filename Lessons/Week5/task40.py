lst = list(map(int, input().split()))

last0 = -1
for i in range(len(lst)):
    if lst[i] == 0 and last0 == -1:
        last0 = i
    if lst[i] != 0 and last0 != -1:
        lst[i], lst[last0] = lst[last0], lst[i]
        last0 += 1

print(*lst)
