s = input()
part1 = s[:s.find('h')]
part2 = s[len(s) - s[::-1].find('h'):]
print(part1 + part2)
