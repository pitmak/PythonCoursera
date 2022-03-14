import itertools

m = [[0, 2, 3, 24, 16],
     [4, 8, 27, 23, 4],
     [10, 26, 14, 7, 9],
     [36, 12, 3, 10, 17],
     [14, 1, 9, 12, 0]]


def get_answer(row, col):
    print(row, col)
    if row == col == 4:
        return m[4][4], ''
    elif row == 4:
        curr_sum, curr_answer = get_answer(4, col + 1)
        return m[row][col] + curr_sum, 'R' + curr_answer
    elif col == 4:
        curr_sum, curr_answer = get_answer(row + 1, 4)
        return m[row][col] + curr_sum, 'L' + curr_answer
    else:
        curr_sum_r, curr_answer_r = get_answer(row, col + 1)
        curr_sum_l, curr_answer_l = get_answer(row + 1, col)
        if curr_sum_r > curr_sum_l:
            return m[row][col] + curr_sum_r, 'R' + curr_answer_r
        else:
            return m[row][col] + curr_sum_l, 'L' + curr_answer_l


max_sum, answer = get_answer(0, 0)
print(max_sum)
print(answer)

for elem in itertools.product('RL', repeat=8):
    print(''.join(elem))
