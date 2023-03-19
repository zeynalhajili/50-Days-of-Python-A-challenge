"""
Write a function called convert_add that takes a list of 
strings as an argument and converts it to integers and sums the list. 
For example ["1", "4", "9"] should be converted to [1, 3, 5] and summed to 9.
"""

def convert_add(list_to_add):
    total = 0
    for i in list_to_add:
        total = float(i) + total
    return f'{(total):.2f}'

print(convert_add(["1.1","1.3","4"]))
print(convert_add(["1.1","1.3"]))
print(convert_add(["1", "3","11","788","7777","1.1","1.898787"]))