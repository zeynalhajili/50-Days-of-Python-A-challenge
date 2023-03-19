"""
Day 8: Odd and Even
Write a function called odd_even that has one parameter and takes a list of numbers 
as an argument. The function returns the difference between the largest even number 
in the list and the smallest odd number in the list. For example, if you pass 
[1,2,4,6] as an argument the function should return 6 -1= 5.
"""

def odd_even(list_provided):
    odd_numbers_list =[]
    even_numbers_list =[]
    for i in list_provided:
        if i % 2 == 0:
            even_numbers_list.append(i)
        else:
            odd_numbers_list.append(i)

    return max(even_numbers_list) - min(odd_numbers_list)

print(odd_even([1,2,3,4,5,10,12,100]))
print(odd_even([1,-99,3,4,5,10,12,100]))


# def odd_even(list_provided):
#     min_odd = None
#     max_even = None
    
#     for i in list_provided:
#         if i % 2 == 0 and (max_even is None or i > max_even):
#             max_even = i
#         elif i % 2 == 1 and (min_odd is None or i < min_odd):
#             min_odd = i
    
#     return max_even - min_odd if min_odd is not None and max_even is not None else 0