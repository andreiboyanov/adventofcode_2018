import os

all_leters = "abcdefghijklmnopqrstuvwxyz"

data = open(os.path.join(os.path.dirname(__file__), os.pardir, "input", "day2.txt")).read().strip()
codes = data.split("\n")

# codes = [
#     "abcdef",
#     "bababc",
#     "abbcde",
#     "abcccd",
#     "aabcdd",
#     "abcdee",
#     "ababab",
# ]


twos = threes = 0
for code in codes:
    found_two = found_three = False
    for letter in all_leters:
        count = code.count(letter)
        if not found_two and count == 2:
            found_two = True
            twos += 1
        elif not found_three and count == 3:
            found_three = True
            threes += 1
        if found_two and found_three:
          break
print(twos * threes)