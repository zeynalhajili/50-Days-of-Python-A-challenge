"""
Day 23: Simple Calculator
Create a simple calculator. The calculator should be able to perform basic math 
operations, add, subtract, divide and multiply. The calculator should take input 
from users. The calculator should be able to handle ZeroDivisionError, NameError, and
ValueError.
"""

def calculator():
    # take input and choose operator
    first_number = input("Please enter first number: ")
    second_number = input("Please enter second number: ")
    operator = input("To add, press 1. To subtract, press 2. To divide, press 3. To multiply, press 4.\n")

    result = None

    if operator == "1":
        result = float(first_number) + float(second_number)
    elif operator == "2":
        result = float(first_number) - float(second_number)
    elif operator == "3":
        try:
            result = f'Result is {float(first_number) / float(second_number):.1f}'
        except ZeroDivisionError:
            return "Error: Cannot divide by zero !"
    else:
        result = float(first_number) * float(second_number)
    
    return result

print(calculator())
