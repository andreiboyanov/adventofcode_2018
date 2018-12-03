import os


data = open(os.path.join(os.path.dirname(__file__), os.pardir, "input", "day1.txt")).read().strip()

numbers = list(map(int, data.split("\n")))
number_count = len(numbers)

frequencies = [0, ]
index = 0
frequency_index = 0
new_frequency = 0
while True:
    new_frequency = frequencies[frequency_index] + numbers[index]
    if new_frequency in frequencies:
        break
    index += 1
    frequency_index += 1
    if index >= number_count:
        index = 0
    frequencies.append(new_frequency)
print(new_frequency)