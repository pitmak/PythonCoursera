maxes = [-1] * 12

with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        n1, n2, clas, ball = line.split()
        clas = int(clas)
        ball = int(ball)
        if ball > maxes[clas]:
            maxes[clas] = ball

for i in 9, 10, 11:
    print(maxes[i], end=' ')
