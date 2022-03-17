with open('input.txt', 'r', encoding='utf8') as file:
    store = set(file.read().split())
    print(len(store))
