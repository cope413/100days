import string

input_data = r'C:\Users\Taylor\Downloads\adventofcode.com_2022_day_3_input.txt'

rucksacks = []

with open(input_data) as my_file:
    contents = my_file.read().splitlines()
    for n in contents:
        rucksacks.append(n)

container_1 = []
container_2 = []
combo = []

priorities = list(string.ascii_lowercase) + list(string.ascii_uppercase)
values = []
for x in range(1, 53):
    values.append(x)

translation = {priorities: values for priorities, values in zip(priorities, values)}

for line in rucksacks:
    amount = len(line)
    half = int(amount / 2)  # first bag range = (0,{half}), second = ({half}, {amount})
    box_1 = line[0:half]
    box_2 = line[half:amount]
    container_1.append(box_1)
    container_2.append(box_2)

no_dupes1 = []
no_dupes2 = []

for x in container_1:
    a = set(x)
    no_dupes1.append(a)
for y in container_2:
    b = set(y)
    no_dupes2.append(b)

sum_of_rucksacks = []
for x in range(0, len(container_1)):
    for y in no_dupes1[x]:
        if y in no_dupes2[x]:
            combo.append(y)

for val in combo:
    x = translation.get(val)
    sum_of_rucksacks.append(x)

print(f"Sum of priorities of item types: {sum(sum_of_rucksacks)}")
