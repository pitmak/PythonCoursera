p = int(input())
x = int(input())
y = int(input())

depo = (x * 100 + y) * (100 + p) // 100
print(depo // 100, depo % 100)
