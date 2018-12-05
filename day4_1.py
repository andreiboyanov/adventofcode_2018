import os

DATE_LENGTH = len("[1518-10-03 00:47]")

data = open(os.path.join(os.path.dirname(__file__), os.pardir, "input", "day4.txt")).read().strip()
data = data.split("\n")
data = sorted(data, key=lambda record: record[: DATE_LENGTH - 1])

# [1518-10-03 00:47] falls asleep
# [1518-07-26 23:50] Guard #487 begins shift
# [1518-06-22 00:48] wakes up
# [1518-08-21 00:30] falls asleep
# [1518-11-21 00:55] wakes up
# [1518-05-30 00:06] falls asleep

day_record = list()
guard = None
guards = dict()
asleep_time = -1
awake_time = -1
for record in data:
    date = record[:DATE_LENGTH]
    day = date[1:-1]
    minutes = int(date[len("[1518-10-03 00:"):-1])
    text = record[DATE_LENGTH + 1:]

    if text.startswith("Guard"):
        if guard is not None:
            guards[guard][0] += sum([r[3] for r in day_record])
            guards[guard][1].append(day_record)
        day_record = list()
        guard = text.split(" ")[1]
        if guard not in guards:
            guards[guard] = [0, list()]
    elif text.startswith("falls"):
        asleep_time = minutes
    elif text.startswith("wakes"):
        awake_time = minutes
        day_record.append([guard, asleep_time, awake_time, awake_time - asleep_time])
if guard is not None:
    guards[guard][0] += sum([r[3] for r in day_record])
    guards[guard][1].append(day_record)

guard_id = sorted(guards, key=lambda guard_id: guards[guard_id][0], reverse=True)[0]
minutes = dict()
for day in guards[guard_id][1]:
    for record in day:
        for minute in range(record[1], record[2]):
            if minute in minutes:
                minutes[minute] += 1
            else:
                minutes[minute] = 1

print(set(guards.keys()))
