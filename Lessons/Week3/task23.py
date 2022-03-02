s = input()
p1 = s.find('h')
p2 = s.rfind('h')
if p1 == p2:
    print(s)
else:
    print(s[:p1 + 1] + s[p1 + 1:p2].replace('h', 'H') + s[p2:])
