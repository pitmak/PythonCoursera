party_par = []
with open('input.txt', 'r', encoding='utf8') as file:
    n, k = map(int, file.readline().split())
    for i in range(k):
        party_par.append(tuple(map(int, file.readline().split())))


def check_strike(day):
    for a, b in party_par:
        if day >= a and (day - a) % b == 0:
            return True
    return False


count = 0
for i in range(1, n + 1):
    if i % 7 == 6 or i % 7 == 0:
        continue
    if check_strike(i):
        count += 1

print(count)
