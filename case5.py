prices = [100, 300, 50, 200, 100]
quantities = [2, 2, 5, 3, 1]
budgets = [500, 500, 250, 500, 100]

for i in range(5):
    total = prices[i] * quantities[i]

    print("Test Case:", i + 1)
    print("Total Cost:", total)
    print("Budget:", budgets[i])

    if total <= budgets[i]:
        print("Shopping Within Budget")
    else:
        print("Shopping Exceeds Budget")
        print("Extra Amount:", total - budgets[i])