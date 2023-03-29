"""
Day 23: Simple Calculator
Create a simple calculator. The calculator should be able to perform basic math 
operations, add, subtract, divide and multiply. The calculator should take input 
from users. The calculator should be able to handle ZeroDivisionError, NameError, and
ValueError.
"""

# function to check if input is valid number 

def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def calculator():

    # take input and choose operator
    first_number = input("Please enter first number: ")
    second_number = input("Please enter second number: ")
    operator = input("To add, press 1. To subtract, press 2. To divide, press 3. To multiply, press 4.\n")

    result = None # The issue might be that if the user selects the division operator and a ZeroDivisionError occurs, 
    #the except block prints an error message but does not return a value. 
    #This means that result is not defined in this case, causing an UnboundLocalError when the function attempts to return it.

    # validate the input 

    if not is_valid_number(first_number) or not is_valid_number(second_number):
        raise ValueError("Please enter valid number to continue!")

    # perform calculation based on operator

    if operator == "1":
        if float(first_number) and float(second_number) > 0:
            result = f'Result is {float(first_number) + float(second_number):.1f}'
        else:
            raise ValueError("Please work only with positive numbers!")    
    elif operator == "2":
        result = float(first_number) - float(second_number)
    elif operator == "3":
        try:
            result = f'Result is {float(first_number) / float(second_number):.1f}'
        except ZeroDivisionError:
            return "Error: Cannot divide by zero !"
    else:
        result = f'Result is {float(first_number) * float(second_number):.1f}'
    
    return result


if __name__ == '__main__':
    print(calculator())

