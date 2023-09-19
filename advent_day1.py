raw_calories = r'C:\Users\Taylor\Downloads\adventofcode.com_2022_day_1_input.txt'

calorie_list = []
calorie_sums = []
dummy_value = -5
sub_total = 0

# Open raw data and read lines into list.
# Change strings into integers and replace empty lines with dummy value for sorting
f = open(raw_calories)
text = f.read().splitlines()
for n in text:
    if n != '':
        calorie_list.append(int(n))
    else:
        calorie_list.append(dummy_value)

# look for dummy value in raw data, sum up all values between dummy values and add the sums to a list
for x in range(0, len(calorie_list)):
    if calorie_list[x] != dummy_value:
        sub_total += calorie_list[x]
    elif calorie_list[x] == dummy_value:
        calorie_sums.append(sub_total)
        sub_total = 0

# Day 1 part 2 asks for sum of top 3 calorie carriers
top_3 = []
loop = 3
while loop > 0:
    top_3.append(max(calorie_sums))
    calorie_sums.remove(max(calorie_sums))
    loop -= 1


print(f"Top calorie load is : {max(calorie_sums)}")
print(f"Sum of top 3 carriers is: {sum(top_3)}")


