"""
Day 7: A String Range
Write a function called string_range that takes a single number and returns a string
of its range. The string characters should be separated by dots(.) For example, 
if you pass 6 as an argument, your function should return ‘0.1.2.3.4.5’.
"""

def string_range(initial_number):
    list_with_numbers= []
    for i in range(initial_number):
        list_with_numbers.append(i)
    print(list_with_numbers)

string_range(7)
string_range(9)