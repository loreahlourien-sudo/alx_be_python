Monthly_Income = int(input("Enter your monthly income:"))
Monthly_Expenses = int(input("Enter your total monthly expenses:"))
Monthly_Saving = Monthly_Income - Monthly_Expenses
Projected_Savings = Monthly_Saving * 12 + (Monthly_Saving * 12 * 0.05)
print("Enter your monthly income:",Monthly_Income,)
print("Enter your total monthly expenses:",Monthly_Expenses,)
print("Your monthly savings are $",Monthly_Saving,)
print("Projected savings after one year, with interest, is: $",Projected_Savings,)