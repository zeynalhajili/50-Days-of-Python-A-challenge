"""
Day 9: Biggest Odd Number
Create a function called biggest_odd that takes a string of numbers and returns the 
biggest odd number in the list. For example, if you pass ‘23569’ as an argument, 
your function should return 9. Use list comprehension.
"""

# def biggest_odd(input_string):
#     biggest_number = None
#     for i in input_string:
#         if int(i) % 2 == 1:
#             if biggest_number is None or i > biggest_number:
#                 biggest_number = i
#     print(biggest_number)

def biggest_odd(input_string):
    odd_numbers = [int(i) for i in input_string if int(i) % 2 == 1]
    biggest_odd =max(odd_numbers)
    return biggest_odd

print(biggest_odd("12345"))
print(biggest_odd("1234587"))
