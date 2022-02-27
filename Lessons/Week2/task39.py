count = 1
max = int(input())
while True:
    n = int(input())
    if n == 0:
        break
    if n == max:
        count += 1
    elif n > max:
        max = n
        count = 1
print(count)
