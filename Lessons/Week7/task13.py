with open('input.txt', 'r', encoding='utf8') as file:
    countries = []
    towns = {}
    n = int(file.readline())
    for i in range(n):
        line = file.readline().split()
        countries.append(line[0])
        for j in range(1, len(line)):
            towns[line[j]] = len(countries) - 1
    m = int(file.readline())
    for i in range(m):
        print(countries[towns[file.readline().strip()]])
