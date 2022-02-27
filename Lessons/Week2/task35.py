count = 0
sum = 0
while True:
    n = int(input())
    if n != 0:
        count += 1
        sum += n
    else:
        break
print(sum / count)
