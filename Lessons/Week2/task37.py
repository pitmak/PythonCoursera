count = 0
prev = int(input())
while True:
    n = int(input())
    if n == 0:
        break
    if n > prev:
        count += 1
    prev = n
print(count)
