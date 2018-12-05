import os

all_leters = "abcdefghijklmnopqrstuvwxyz"
orig_data = open(os.path.join(os.path.dirname(__file__), os.pardir, "input", "day5.txt")).read().strip()

min_len = 9999999999
data = None
for letter in all_leters:
    data = orig_data.replace(letter, "")
    data = data.replace(letter.upper(), "")

    i = 0
    len_data = len(data)
    while i < len_data-1:
        if (data[i+1].isupper() and data[i] == data[i+1].lower()) or (data[i+1].islower() and data[i] == data[i+1].upper()):
            data = data[:i] + data[i+2:]
            len_data -= 2
            if i > 0:
                i -= 1
        else:
            i += 1
    min_len = min(min_len, len_data)

print(min_len)
print(len(data))