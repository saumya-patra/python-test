# Get details of a loan
money_owed = float(input("Enter the amount of money owed, in dollars: "))
interest_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
payment = float(input("Enter the monthly payment amount, in dollars: "))
months = int(input("Enter the number of months to pay off the loan: "))
monthly_interest_rate = interest_rate / 12

#Calculate the intrest to pay
interest_paid = money_owed * monthly_interest_rate

#Add interest to the money owed
money_owed += interest_paid

#Make the payment
money_owed -= payment

print("After " + str(months) + " months, the remaining balance is: $" + str(round(money_owed, 2)))
print("Total interest paid: $" + str(round(interest_paid, 2)))