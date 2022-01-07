# 1. Collect user data - annual salary, portion saved each month as a %, total cost of home
# 2. calculate down payment needed
# 3. define current savings (default to 0)
# 3a. Calculate monthly salary (annual / 12)
# 4. Calculate the monthly portion saved and add it to savings - grow savings each month, keep count of the savings
# 5. calculate growth over time of savings  (0.04% annualy) and monthly savings (that div 12) as you save
# 6. main loop is while downpayment >= savings

# define global variables

annual_salary = 0 # how much you make each year
portion_saved = 0 # how much of your salary will we save (as a decimal)
total_cost = 0 # the total cost of the home
current_savings = 0 # how much you've saved so far
r = .04 # annual return on investments
months = 0 # how many months does it take to get your down payment saved

# user input section
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

portion_down_payment = total_cost * .25 # down payment is 25% of total house cost

# calulate the months
while portion_down_payment > current_savings:
    months += 1
    monthly_salary = annual_salary / 12
    monthly_savings = monthly_salary * portion_saved
    investment_return = current_savings * (r / 12)
    current_savings = current_savings + investment_return + monthly_savings
    print("months:", months)
    print("monthly savings:", monthly_savings)
    print("investment return:", investment_return)
    print('current savings', current_savings)
    print('_______________')

print("Number of months: ", months)