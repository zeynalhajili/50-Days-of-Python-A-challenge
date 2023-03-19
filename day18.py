"""
Day 18: Any Number of Arguments
Write a function called any_number that can receive any number of arguments(integers 
and floats) and return the average of those integers. If you pass 12, 90, 12, 34 as 
arguments your function should return 37.0 as average. If you pass 12, 90 your 
function should return 51.0 as average.
"""

def any_number(*any_numbers):
    average_numnber = sum(any_numbers)/len(any_numbers)
    return average_numnber

print(any_number(1,3,4,5,9,101,112,10000))

