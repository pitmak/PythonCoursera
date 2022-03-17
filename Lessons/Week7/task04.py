store = set()
for elem in input().split():
    print('YES' if elem in store else "NO")
    store.add(elem)
