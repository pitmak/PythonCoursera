s = input()
pos = s.find('f')
if pos == -1:
    print(-2)
else:
    pos = s.find('f', pos + 1)
    if pos == -1:
        print(-1)
    else:
        print(pos)
