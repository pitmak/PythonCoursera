s = input()

p1 = s.find('h') + 1
p2 = len(s) - s[::-1].find('h') - 1

print(s[:p1] + s[p1:p2] + s[p1:p2] + s[p2:])
