"""
Day 24: Average Calories
Create a function called average_calories that calculates the average calories intake
of a user. The function should ask the user to input their calories intake for any 
number of days and once they hit ‘done’ it should calculate and return the average 
intake.
"""


# Day 1: 2000 calories
# Day 2: 1800 calories
# Day 3: 2200 calories
# Day 4: 1900 calories
# Day 5: done

def average_calories():
    list_calory = []
    while True:
        try:
            input_calory =input("Please enter calory: ")
            if input_calory == "done":
                break
            else:
                list_calory.append(int(input_calory))
        except ValueError:
            print("Please enter valid number!!!")

    return f'Average calory is {sum(list_calory) / len(list_calory):.0f} kcal!'

print(average_calories())

