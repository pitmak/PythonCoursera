initial_list = []
total_votes = 0
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        last_space = line.rfind(' ')
        votes = int(line[last_space:])
        initial_list.append((line[:last_space], votes))
        total_votes += votes
feq = total_votes / 450
party_dict = {}
second_list = []
total_places = 0
for party, votes in initial_list:
    places = int(votes / feq)
    party_dict[party] = places
    total_places += places
    second_list.append((votes / feq - places, votes, party))
second_list.sort(reverse=True)
for i in range(450 - total_places):
    party_dict[second_list[i][2]] += 1
for elem in initial_list:
    print(elem[0], party_dict[elem[0]])
