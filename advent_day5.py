input_data = r'C:\Users\Taylor\Downloads\adventofcode.com_2022_day_5_input.txt'
move_data = r'C:\Users\Taylor\Downloads\day_5_moves.txt'

stacks = {
    1: ['R', 'G', 'J', 'B', 'T', 'V', 'Z'],
    2: ['J', 'R', 'V', 'L'],
    3: ['S', 'Q', 'F'],
    4: ['Z', 'H', 'N', 'L', 'F', 'V', 'Q', 'G'],
    5: ['R', 'Q', 'T', 'J', 'C', 'S', 'M', 'W'],
    6: ['S', 'W', 'T', 'C', 'H', 'F'],
    7: ['D', 'Z', 'C', 'V', 'F', 'N', 'J'],
    8: ['L', 'G', 'Z', 'D', 'W', 'R', 'F', 'Q'],
    9: ['J', 'B', 'W', 'V', 'P']
}

with open(move_data) as f:
    data = f.read().split()
    moves = data

# Words "Move", "From", and "To" removed from input data
remove_words = [x for x in moves if x != 'move' and x != 'from' and x != 'to']
moves = remove_words


# Format for Moves List: [[X, Y, Z]] move Number(X) from Column (Y) to Column (Z)

def group_into_3(moves_list, group_size):
    result = []
    for i in range(0, len(moves_list), group_size):
        result.append(moves_list[i:i + group_size])
    return result


grouped_moves = group_into_3(moves, 3)
# print(grouped_moves)
all_moves = [all_moves[0] for all_moves in grouped_moves]
from_column = [from_column[1] for from_column in grouped_moves]
to_column = [to_column[2] for to_column in grouped_moves]

# print(all_moves)
# print(from_column)
# print(to_column)


#  Format for Moves List: [[X, Y, Z]] = move Number(X) from Column (Y) to Column (Z) - starting with Y[-1]
#  get N value from dictionary for Col_Z[-1]
#  remove N values from dictionary for COL_Z[-1]
#  add/append N value to Col_Y. Repeat X times

def move_containers(number_of_moves, subtract_column, add_column):
    for x in range(0, int(number_of_moves)):
        moving_box = stacks[int(subtract_column)][-1]
        stacks[int(add_column)].append(moving_box)
        stacks[int(subtract_column)].pop(-1)


for x in range(0, len(all_moves)):
    move_containers(all_moves[x], from_column[x], to_column[x])

for x in stacks:
    print(stacks[x][-1])
