"""
Day 3: Register Check
Write a function called register_check that checks how many students are in school. 
The function takes a dictionary as a parameter. If the student is in school, the 
dictionary says ‘yes’. If the student is not in school, the dictionary says ‘no’. 
Your function should return the number of students in school. Use the dictionary 
below. Your function should return 3.
register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}
"""

def register_check(register):
    total_numnber_of_students = 0
    for i in register.values(): # iterate for dict value
        if i == "yes":
            total_numnber_of_students+=1
    return total_numnber_of_students

students_in_school_at_weekdays = register_check({'Michael':'yes','John': 'no', 'Peter':'no', 'Mary': 'yes'})
students_in_school_at_weekend = register_check({'Michael':'no','John': 'no', 'Peter':'no', 'Mary': 'no'})
print("Total number of students in school is {} on weekdays".format(register_check({'Michael':'yes','John': 'yes', 'Peter':'yes', 'Mary': 'yes'}))) # formmating with format method
print(f"Total number of students in school is {students_in_school_at_weekend} on weekends") # formatting with f-string

