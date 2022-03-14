with open('input.txt', 'r', encoding='utf8') as file:
    maxes = [-1] * 12
    count = [-1] * 12
    for line in file:
        n1, n2, clas, ball = line.split()
        clas = int(clas)
        ball = int(ball)
        if ball > maxes[clas]:
            maxes[clas] = ball
            count[clas] = 1
        elif ball == maxes[clas]:
            count[clas] += 1
    for i in 9, 10, 11:
        print(count[i], end=' ')
