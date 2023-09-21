input_data = r'C:\Users\Taylor\Downloads\adventofcode.com_2022_day_4_input.txt'

with open(input_data) as f:
    assignments = f.read().splitlines()

# print(assignments)

new = []

for line in assignments:
    a = line.split(',')
    new.append(a)

# print(new)
no_dash = []

for pair in new:
    for line in pair:
        a = line.split('-')
        elf1_beginning = int(a[0])
        elf1_end = int(a[1])
        group = [elf1_beginning, elf1_end]
        no_dash.append(group)

final = []
for x in range(0, len(no_dash), 2):
    test = no_dash[x] + no_dash[x + 1]
    final.append(test)


dupe_count = 0
for x in final:
    if x[0] <= x[2] and x[1] >= x[3]:
        dupe_count += 1
    elif x[2] <= x[0] and x[3] >= x[1]:
        dupe_count += 1

overlap_count = 0
# Part 2 - overlap  [x[0], x[1], x[2], x[3]]
for x in final:
    if x[2] in range(x[0], x[1]+1):
        overlap_count += 1
    elif x[0] in range(x[2], x[3]+1):
        overlap_count += 1
    elif x[1] in range(x[2], x[3]+1):
        overlap_count += 1
    elif x[3] in range(x[0], x[1]+1):
        overlap_count += 1


print(dupe_count)
print(overlap_count)

