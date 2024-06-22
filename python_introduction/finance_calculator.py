# Personal Finance Calculator

#User Input for Financial Details:
monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings:
monthly_savings = monthly_income - total_monthly_expenses

# Projecting Annual Savings:
annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")
