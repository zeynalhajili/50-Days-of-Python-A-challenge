"""
Write a function called divide_or_square that takes one argument (a number), 
and returns the square root of the number if it is divisible by 5, returns
its remainder if it is not divisible by 5. For example, if you pass 10 as
an argument, then your function should return 3.16 as the square root.
"""
from math import sqrt

def divide_or_square(number):
    if number % 5  == 0:
        return f'{sqrt(number):.2f}' # The :.2f part of the expression specifies that the resulting 
                                    # value should be formatted as a floating point number 
                                    # with two decimal places.
    else:
        return number % 5 

print(divide_or_square(35))
print(divide_or_square(31))
print(divide_or_square(25))
print(divide_or_square(105))
print(divide_or_square(15))
print(divide_or_square(33))