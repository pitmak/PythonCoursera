a = int(input())
b = int(input())
c = int(input())

hyp = 0
kat1 = 0
kat2 = 0

if a > b:
    if a > c:
        hyp = a
        kat1 = c
    else:
        hyp = c
        kat1 = a
    kat2 = b
else:
    if b > c:
        hyp = b
        kat1 = c
    else:
        hyp = c
        kat1 = b
    kat2 = a

if hyp >= kat1 + kat2:
    print('impossible')
elif hyp * hyp == kat1 * kat1 + kat2 * kat2:
    print('rectangular')
elif hyp * hyp < kat1 * kat1 + kat2 * kat2:
    print('acute')
else:
    print('obtuse')
