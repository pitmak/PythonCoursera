s = input()
ind1 = s.find('f')
if ind1 != -1:
    ind2 = len(s) - s[::-1].find('f') - 1
    if ind1 == ind2:
        print(ind1)
    else:
        print(ind1, ind2)
