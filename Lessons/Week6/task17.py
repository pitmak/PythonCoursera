with open('input.txt', 'r', encoding='utf8') as file:
    first = [0] * 12
    second = [0] * 12
    for line in file:
        n1, n2, clas, ball = line.split()
        clas = int(clas)
        ball = int(ball)
        if ball > first[clas]:
            second[clas] = first[clas]
            first[clas] = ball
        elif ball > second[clas] and ball != first[clas]:
            second[clas] = ball
    for i in 9, 10, 11:
        print(second[i], end=' ')
