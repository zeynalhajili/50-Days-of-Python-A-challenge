"""
Day 22: Add Under_Score
Create three functions. The first called add_hash takes a string and adds a 
hash # between the words. The second function called add_underscore removes the 
hash(#) and replaces it with an underscore ( _ ) The third function called 
remove_underscore, removes the underscore and replaces it with nothing. 
if you pass ‘Python’ as an argument for the three functions, and you call them at 
the same time like: print(remove_underscore(add_underscore(add_hash('Python'))))
it should return ‘Python’.
"""
def add_hash(input_string):
    new_hashed_string = "#".join(input_string)
    return new_hashed_string

def add_underscore(input_string):
    new_replaced_string = input_string.replace("#","_")
    return new_replaced_string

def remove_underscore(input_string):
    final_string = input_string.replace("_","")
    return final_string

input = "Azerbaijan"
print(add_hash(input))
print(add_underscore(add_hash(input)))
print(remove_underscore(add_underscore(add_hash(input))))