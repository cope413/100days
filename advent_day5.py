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


remove_move = [x for x in moves if x != 'move']
remove_from = [y for y in remove_move if y != 'from']
remove_to = [z for z in remove_from if z != 'to']

moves = remove_to  # All moves with "Move", "From", and "To" removed from input data


# Format for Moves List: [[X, Y, Z]] move Number(X) from Column (Y) to Column (Z)

def group_into_3(moves_list, group_size):
    result = []
    for i in range(0, len(moves_list), group_size):
        result.append(moves_list[i:i + group_size])
    return result


grouped_moves = group_into_3(moves, 3)
print(grouped_moves)
# TODO : Format for Moves List: [[X, Y, Z]] = move Number(X) from Column (Y) to Column (Z) - starting with Y[-1]
# TODO : get N value from dictionary for Col_Z[-1]
# TODO : remove N values from dictionary for COL_Z[-1]
# TODO : add/append N value to Col_Y. Repeat X times

