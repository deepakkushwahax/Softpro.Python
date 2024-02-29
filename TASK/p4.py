# Taking user input for number of days
days = int(input("Enter the number of days: "))

# Calculating years, months, and remaining days
years = days // 365
months = (days % 365) // 30
remaining_days = (days % 365) % 30

# Printing the results
print("Years:", years)
print("Months:", months)
print("Days:", remaining_days)