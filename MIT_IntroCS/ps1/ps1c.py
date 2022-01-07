"""
if you fix it at 36 months, you can submit to the fucntion and see what your savings is - if it's within 100 of 25% then you're ok.
if not, then bisect and submit the next savings %

"""


def savings_amount(year_salary, percent_saved):
    semi_annual_raise = .07  # percent raise every 6 months
    investment_return_rate = 0.04
    your_savings = 0  # how much you've saved so far
    savings_months = 0

    while savings_months < 36:
        savings_months += 1
        monthly_salary = year_salary / 12
        monthly_savings = monthly_salary * (percent_saved/10000)
        investment_growth = your_savings * (investment_return_rate / 12)
        your_savings = your_savings + investment_growth + monthly_savings
        if savings_months % 6 == 0:
            year_salary = year_salary * (1 + semi_annual_raise)
        print("annual salary: ", year_salary)
        print("months:", savings_months)
        print("percent saved/100:", (percent_saved/100))
        print("monthly savings:", monthly_savings)
        print("investment return:", investment_growth)
        print('current savings:', your_savings)
        print('_______________')
    return your_savings


total_cost = 1000000  # the total cost of the home is $1M
portion_down_payment = total_cost * .25  # down payment is 25% of total house cost
step = 0  # number of steps in the bisection search
low = 0
high = 10000
months = 0
annual_salary = 0  # how much you make each year
savings_rate = (low+high)/2
current_savings = 0

annual_salary = int(input("Enter your starting salary: "))

while abs(portion_down_payment - current_savings) > 100:
    if (high - low) > 1:
        print("low:", low, "high:", high, "months: ", months, "step: ", step, "savings rate:", savings_rate)
        step += 1
        current_savings = savings_amount(annual_salary, savings_rate)
        if current_savings < portion_down_payment:
            low = savings_rate
            print("Change Low")
        else:
            high = savings_rate
            print("Change High")
        savings_rate = (high + low) / 2
        print("savings rate:", savings_rate)
        print("The best savings rate is: ", savings_rate)
        print("Steps in bisection search: ", step)
    else:
        print ("You can't save enough per month at that salary in 36 months")
        break