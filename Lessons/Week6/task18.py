dist = sorted(list(map(int, input().split())))
cost = sorted(list(map(int, input().split())), reverse=True)

total = 0
for i in range(len(dist)):
    total += dist[i] * cost[i]

print(total)
