lst = []

with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        lst.append(tuple(line.split()))

for item in sorted(lst):
    print(item[0], item[1], item[3])

print(lst)
