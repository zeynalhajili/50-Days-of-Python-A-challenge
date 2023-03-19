"""
Day 20: Capitalize First Letter
Write a function called capitalize. This function takes a string as an argument and 
capitalizes the first letter of each word. For example, ‘i like learning’ becomes
‘I Like Learning’.
"""

def capitalize(input_sentence):
    temporary_list = []
    for word in input_sentence.split(" "):
        temporary_list.append(word.capitalize())
    return " ".join(temporary_list)

print(capitalize("Zeunal sasa bayraminiz mubarek ikar olsun qaqalar"))




