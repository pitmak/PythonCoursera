count = 0
while True:
    n = int(input())
    if n != 0:
        if n % 2 == 0:
            count += 1
    else:
        break
print(count)
