"""
Write a function called count_dots. This function takes a string separated by dots as
 a parameter and counts how many dots are in the string. For example, ‘h.e.l.p.’ 
 should return 4 dots, and ‘he.lp.’ should return 2 dots.
Extra Challenge: Your Age in Minutes
b. Write a function called age_in_minutes that tells a user how old they are in 
minutes. Your code should ask the user to enter their year of birth, and it should 
return their age in minutes (by subtracting their year of birth to the current year).
 Here are things to look out for:
a. The user can only input a 4 digit year of birth. For example, 1930 is a valid year
. However, entering any number longer or less than 4 digits long should render input 
invalid. Notify the user to input a four digits number.
b. If a user enters a year before 1900, your code should tell the user that input is 
invalid. If the user enters the year after the current year, the code should tell the
 user, to input a valid year.
The code should run until the user inputs a valid year. Your function should return 
the user's age in minutes. For example, if someone enters 1930, as their year of birth
your function should return:
You are 48,355,200 minutes old.
"""

"""
SOLUTION1
"""

def count_dots(input_string):
    empty_list= []
    for i in input_string:
        if i == ".":
            empty_list.append(i)
    print("In this string we have {} dots".format(len(empty_list)))

# count_dots("...........................121212..............")

"""
SOLUTION2
"""
# def count_dots(input_string):
#     num_dots = input_string.count(".")
#     print(f"In this string we have {num_dots} dots")

# count_dots("...........................121212..............")

from datetime import date

def age_in_minutes():
    current_year =date.today().year
    birth_year =int(input("Please enter when you were born: "))
    while birth_year > 1900:
        delta_year_with_minute = (current_year -birth_year)*365*24*60
        print(f'You have lives {delta_year_with_minute:,.0f} minutes ')
        break
    else:
        print("Please enter valid year!")
age_in_minutes()

