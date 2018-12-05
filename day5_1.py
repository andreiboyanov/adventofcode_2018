import os

data = open(os.path.join(os.path.dirname(__file__), os.pardir, "input", "day5.txt")).read().strip()
# data = "dabAcCaCBAcCcaDAa"
# data = "IiXZRrzHhxXxayYAFuUNiInEeSsaAYGgOeEowWHdtYyYyDdTqQCRfFrcDuUGggfFGXfjJFNCcnhHlLAaHhxocCVvLlzeEUMWwmnNuZhbBHkKbSsBtTwWHRrNnhORU"

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

print(data)
print(len(data))