## 1pt Rock, 2pt Paper, 3pt Scissors
## 0pts loss, 3pt draw, 6pt win

strategy_guide = r'C:\Users\Taylor\Downloads\adventofcode.com_2022_day_2_input.txt'
outcomes = []
# Part 1
# scores = {
#     'A X': 4,
#     'A Y': 8,
#     'A Z': 3,
#     'B X': 1,
#     'B Y': 5,
#     'B Z': 9,
#     'C X': 7,
#     'C Y': 2,
#     'C Z': 6,
# }

# Part 2
scores = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7,
}

f = open(strategy_guide)
text = f.read().splitlines()
# print(text)

for n in text:
    if n in scores:
        outcomes.append(scores[n])

print(sum(outcomes))
