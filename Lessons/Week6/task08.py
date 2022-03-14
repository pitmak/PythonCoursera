balls = [0] * 12
counts = [0] * 12

with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        n1, n2, clas, ball = line.split()
        balls[int(clas)] += int(ball)
        counts[int(clas)] += 1

for i in 9, 10, 11:
    print(balls[i] / counts[i], end=' ')
