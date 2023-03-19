"""
Day 17: User Name Generator
Write a function called user_name, that creates a username for the user. The function
should ask a user to input their name. The function should then reverse the name and 
attach a randomly issued number between 0 – 9 at the end of the name. The function 
should return the username.
"""
import random 

def user_name():
    input_name = input("Please input your name please: ")
    random_number =random.randint(0,9)
    return  input_name[::-1] + str(random_number)

print(user_name())