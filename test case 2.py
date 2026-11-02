if len(password) < 8:
    errors.append("Password must contain at least 8 characters")

if not any(ch.isupper() for ch in password):
    errors.append("At least one uppercase letter is required")

if not any(ch.islower() for ch in password):
    errors.append("At least one lowercase letter is required")

if not any(ch.isdigit() for ch in password):
    errors.append("At least one digit is required")

special = "@#$!%&*?"
if not any(ch in special for ch in password):
    errors.append("At least one special character is required")

for i in range(len(password) - 2):
    if password[i] == password[i + 1] == password[i + 2]:
        errors.append("Three consecutive identical characters are not allowed")
        break

if "password" in password.lower():
    errors.append("The word 'password' is not allowed")

if len(errors) == 0:
    print("\nPassword is Valid")
    print("All rules are satisfied")

else:
    print("\nPassword is Invalid")
    print("Reasons:")

    for error in errors:
        print("-", error)