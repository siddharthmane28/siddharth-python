print("==== Monthly expense tracker ====")
n = int(input("enter the number expenses:"))

expenses =[]
total = 0
for i in range(n):
    amount = float(input(f"enter expense{i +1}:"))
    expenses.append(amount)
    total += amount
while True:
    print("\n====Expense Tracker Menu====")
    print("1.Show All Expenses")    
    print("2.Show Total expenses")
    print("3.Add New Expense")
    print("4.Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        print("\nExpense List:")
        for i in range(len(expenses)):
            print(f"Expense {i+1}:{expenses[i]}")   

    elif choice ==2:
        print("Total Monthly Expenses =",total)

    elif choice ==3:
        new_expenses =float(input("Enter new expense:"))
        expenses.append(new_expenses)
        total += new_expenses
        print("Expense added successfully.")

    elif choice ==4:
        print("Thank you for using the monthly expense tracker:")
        break
    else:
        print("invalid choice please try again")                