vilg_count = int(input())
i = 0
vilg_list = []
for elem in map(int, input().split()):
    vilg_list.append((elem, i))
    i += 1

vault_count = int(input())
i = 1
vault_list = []
for elem in map(int, input().split()):
    vault_list.append((elem, i))
    i += 1

vilg_list.sort()
vault_list.sort()

res = [0] * vilg_count

next_vault = 0
for vilg in vilg_list:
    while (next_vault < len(vault_list) - 1 and
           vault_list[next_vault][0] < vilg[0]):
        next_vault += 1
    if next_vault == 0:
        res[vilg[1]] = vault_list[0][1]
    else:
        len1 = abs(vilg[0] - vault_list[next_vault][0])
        len2 = abs(vilg[0] - vault_list[next_vault - 1][0])
        if len1 < len2:
            res[vilg[1]] = vault_list[next_vault][1]
        else:
            res[vilg[1]] = vault_list[next_vault - 1][1]

print(*res)
