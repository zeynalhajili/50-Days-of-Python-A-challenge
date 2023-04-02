"""
Day 25: All the Same
Create a function called all_the_same that takes one argument, a string, a list, or 
a tuple and checks if all the elements are the same. If the elements are the same, 
the function should return True. If not, it should return False. For example, 
[‘Mary’, ‘Mary’, ‘Mary’] should return True.
"""

def all_the_same(my_input):
    # Get the first element of the input sequence and set it as the expected value
    expected = my_input[0]
    
    # Iterate over the remaining elements of the input sequence
    for i in my_input[1:]:
        # If any of the elements does not match the expected value, return False
        if i != expected:
            return False
    
    # If all the elements match the expected value, return True
    return True

# Example usage:
print(all_the_same(["Mary", "Mary", "K"]))  # False
print(all_the_same((1, 1, 1, 1)))          # True
print(all_the_same("aaava"))                # False
