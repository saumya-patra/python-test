sum_expenses = 0
num_expenses = int(input("Enter the number of expenses: "))
expenses = []
for i in range(num_expenses):
    expense = float(input("Enter expense for day " + str(i + 1) + ": "))
    expenses.append(expense)
sum_expenses = sum(expenses)
print("Total expenses: $" + str(sum_expenses))