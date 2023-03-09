"""
Day 6: User Name Generator
Write a function called user_name that generates a username from the user’s email. 
The code should ask the user to input an email and the code should return everything
before the @ sign as their user name. For example, if someone enters ben@gmail.com, 
the code should return ben as their user name
"""

def user_name():
    full_details =input("Please enter e-mail address: ")
    name =full_details.split("@")[0]
    print("Username for provided mail address is {}".format(name.capitalize()))

user_name()
