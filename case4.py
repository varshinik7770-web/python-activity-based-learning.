first_marks = [60, 90, 75, 40, 85]
second_marks = [80, 70, 75, 65, 85]

for i in range(5):
    difference = second_marks[i] - first_marks[i]

    print("Test Case:", i + 1)
    print("First Marks:", first_marks[i])
    print("Second Marks:", second_marks[i])

    if difference > 0:
        print("Performance Improved")
    elif difference < 0:
        print("Performance Declined")
    else:
        print("Performance Unchanged")

    print("Difference:", difference)