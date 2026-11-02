attendance = [85, 70, 80, 90, 80]
marks = [45, 45, 30, 50, 45]
lab = ["yes", "yes", "yes", "no", "yes"]
fees = ["yes", "yes", "yes", "yes", "no"]

for i in range(5):
    eligible = True

    print("Test Case:", i + 1)

    if attendance[i] < 75:
        print("Insufficient Attendance")
        eligible = False

    if marks[i] < 40:
        print("Insufficient Internal Marks")
        eligible = False

    if lab[i] != "yes":
        print("Laboratory Work Incomplete")
        eligible = False

    if fees[i] != "yes":
        print("Fees Not Paid")
        eligible = False

    if eligible:
        print("Eligible for Examination")
    else:
        print("Not Eligible for Examination")