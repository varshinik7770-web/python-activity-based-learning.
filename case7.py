passwords = [
    "Hello123",
    "hello123",
    "HELLO123",
    "HelloWorld",
    "Ab1"
]

for i in range(5):
    password = passwords[i]

    upper = False
    lower = False
    digit = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True

    print("Test Case:", i + 1)

    if len(password) >= 8 and upper and lower and digit:
        print("Valid Password")
    else:
        print("Invalid Password")

        if len(password) < 8:
            print("At least 8 characters required")
        if not upper:
            print("Uppercase letter required")
        if not lower:
            print("Lowercase letter required")
        if not digit:
            print("Digit required")