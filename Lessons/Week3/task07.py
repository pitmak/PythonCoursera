p = int(input())
x = int(input())
y = int(input())
k = int(input())

depo = x * 100 + y

i = 0
while i < k:
    depo += depo * p // 100
    i += 1

print(depo // 100, depo % 100)
