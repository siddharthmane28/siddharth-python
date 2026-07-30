print("***Monthly Expenses***")
expenses = 0.0

while True:
    value = float(input("Enter your value:"))

    if value == -1:
     break
    expenses = expenses+value

    print("Total expenses",expenses)
