"""
Day 11: Are They Equal?
Write a function called equal_strings. The function takes two strings as arguments 
and compares them. If the strings are equal (if they have the same characters and 
have equal length), it should return True, if they are not, it should return False. 
For example, ‘love’ and ‘evol’ should return True.
"""

def equal_strings(string1,string2):
    if (len(string1) == len(string2)) and (sorted(string1) ==sorted(string2)):
        return True
    else:
        return False

print(equal_strings("love", "ovel"))
print(equal_strings("1212", "2131"))
