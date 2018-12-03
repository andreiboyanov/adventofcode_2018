import os


data = open(os.path.join(os.path.dirname(__file__), os.pardir, "input", "day1.txt")).read().strip()
numbers = list(map(int, data.split("\n")))
print(sum(numbers))