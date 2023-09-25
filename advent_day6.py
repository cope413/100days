input_data = r'adventofcode.com_2022_day_6_input.txt'

with open(input_data) as f:
    data = f.read()


start_index = 0

# part 1 = length of unique chars = 4

# while len(set(data[start_index:start_index + 4])) != 4:
#     start_index += 1
#
# print(start_index + 4)


# part 2 = length of unique chars = 14

while len(set(data[start_index:start_index + 14])) != 14:
    start_index += 1

print(start_index + 14)
