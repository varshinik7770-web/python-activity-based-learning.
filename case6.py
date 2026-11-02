timetables = [
    ["9AM", "10AM", "11AM"],
    ["9AM", "9AM", "11AM"],
    ["10AM", "11AM", "12PM"],
    ["9AM", "10AM", "9AM"],
    ["1PM", "2PM", "3PM"]
]

for i in range(5):
    times = timetables[i]
    conflict = False

    for j in range(len(times)):
        for k in range(j + 1, len(times)):
            if times[j] == times[k]:
                conflict = True

    print("Test Case:", i + 1)

    if conflict:
        print("Timetable Conflict Found")
    else:
        print("No Timetable Conflict")