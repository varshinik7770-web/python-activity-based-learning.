balances = [1000, 1000, 1000, 1000, 1000]
choices = ["deposit", "withdraw", "withdraw", "deposit", "withdraw"]
amounts = [500, 300, 1500, 0, 1000]

for i in range(5):
    balance = balances[i]
    amount = amounts[i]
    choice = choices[i]

    if amount <= 0:
        print("Test", i + 1, "Invalid Amount")
    elif choice == "deposit":
        balance = balance + amount
        print("Test", i + 1, "Deposit Successful")
    elif choice == "withdraw":
        if amount <= balance:
            balance = balance - amount
            print("Test", i + 1, "Withdrawal Successful")
        else:
            print("Test", i + 1, "Insufficient Balance")

    print("Final Balance:", balance)