l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())

cond = 0
cond += int(l2 <= l1 <= r2 or l3 <= l1 <= r3)
cond += int(l2 <= r1 <= r2 or l3 <= r1 <= r3)
cond += int(l1 <= l2 <= r1 or l3 <= l2 <= r3)
cond += int(l1 <= r2 <= r1 or l3 <= r2 <= r3)
cond += int(l1 <= l3 <= r1 or l2 <= l3 <= r3)
cond += int(l1 <= r3 <= r1 or l2 <= r3 <= r2)

if cond >= 4:
    print(0)
elif l2 <= l3 <= r2 + r1 - l1 or l3 < l2 <= r3 + r1 - l1:
    print(1)
elif l1 <= l3 <= r1 + r2 - l2 or l3 < l1 <= r3 + r2 - l2:
    print(2)
elif l1 <= l2 <= r1 + r3 - l3 or l2 < l1 <= r2 + r3 - l3:
    print(3)
else:
    print(-1)
