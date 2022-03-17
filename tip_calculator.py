# Author: Peter Baxter
# Date: 3/16/22
# Description: Tip calculator

def tip_calc():
    """Calculates the amount of tip you want to leave. Day 2 of Udemy's 100 days of code"""
    subtotal = float(input("What was the total bill?"))
    tip_desired = (float(input("What percentage would you like to tip? __%"))/100)
    tip = round(subtotal*(tip_desired), 2)
    bill = round(subtotal*(1+tip_desired), 2)
    print(f"Your tip is {tip}, for a total of {bill}. Have a nice day!")

tip_calc()
