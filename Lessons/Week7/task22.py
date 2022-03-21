bank = {}


def deposit(lst):
    if lst[0] not in bank:
        bank[lst[0]] = 0
    bank[lst[0]] += int(lst[1])


def withdraw(lst):
    if lst[0] not in bank:
        bank[lst[0]] = 0
    bank[lst[0]] -= int(lst[1])


def balance(lst):
    if lst[0] in bank:
        print(bank[lst[0]])
    else:
        print('ERROR')


def transfer(lst):
    if lst[0] not in bank:
        bank[lst[0]] = 0
    if lst[1] not in bank:
        bank[lst[1]] = 0
    bank[lst[0]] -= int(lst[2])
    bank[lst[1]] += int(lst[2])


def income(lst):
    for key in bank:
        if bank[key] > 0:
            bank[key] += int(bank[key] * int(lst[0]) / 100)


robo = {'DEPOSIT': deposit,
        'WITHDRAW': withdraw,
        'BALANCE': balance,
        'TRANSFER': transfer,
        'INCOME': income
        }

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.split()
        robo[line[0]](line[1:])
