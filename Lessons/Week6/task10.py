def count_sort(a):
    lst = [0] * 101
    for i in a:
        lst[i] += 1
    c = 0
    for i in range(101):
        for j in range(lst[i]):
            a[c] = i
            c += 1


input_list = list(map(int, input().split()))
count_sort(input_list)
print(*input_list)
