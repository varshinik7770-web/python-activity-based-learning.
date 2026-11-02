key = ["A", "B", "C", "D", "A"]

student_answers = [
    ["A", "B", "C", "D", "A"],
    ["B", "A", "D", "C", "B"],
    ["A", "B", "C", "D", "B"],
    ["A", "B", "", "D", "A"],
    ["A", "X", "C", "X", "A"]
]

for i in range(5):
    answers = student_answers[i]

    correct = 0
    incorrect = 0
    unanswered = 0

    for j in range(5):
        if answers[j] == "":
            unanswered += 1
        elif answers[j] == key[j]:
            correct += 1
        else:
            incorrect += 1

    score = correct * 2

    print("Test Case:", i + 1)
    print("Correct:", correct)
    print("Incorrect:", incorrect)
    print("Unanswered:", unanswered)
    print("Final Score:", score)