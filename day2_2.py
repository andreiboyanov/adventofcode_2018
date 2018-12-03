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


for code1 in codes:
    for code2 in codes:
        count = 0
        code1_length = len(code1)
        if code1_length != len(code2):
            continue
        for i in range(code1_length):
            if code1[i] == code2[i]:
                count += 1
        if count == code1_length - 1:
            common = list()
            for i in range(code1_length):
                if code1[i] == code2[i]:
                    common.append(code1[i])
            print("".join(common))
            exit(0)
