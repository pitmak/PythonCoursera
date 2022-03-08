lst = input().split()
for i in range(1, len(lst)):
    if int(lst[i]) * int(lst[i - 1]) > 0:
        print(lst[i - 1], lst[i])
        break
