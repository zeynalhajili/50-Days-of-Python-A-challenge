"""
Day 14: Flatten the List
Write a function called flat_list that takes one argument, a nested list. The function
 converts the nested list into a one-dimension list. For example [[2,4,5,6]] should 
 return [2,4,5,6].
Extra Challenge: Teacher’s Salary
b. A school has asked you to write a program that will calculate teachers' salaries. 
The program should ask the user to enter the teacher’s name, the number of periods 
taught in a month, and the rate per period. The monthly salary is calculated by 
multiplying the number of periods by the monthly rate. The current monthly rate per 
period is $20. If a teacher has more than 100 periods in a month, everything above 
100 is overtime. Overtime is $25 per period. For example, if a teacher has taught 105
periods, their monthly gross salary should be 2,125. Write a function called 
your_salary that calculates a teacher’s gross salary. The function should return the
teacher’s name, periods taught, and gross salary. Here is how you should format your
output:
Teacher: John Kelly,
Periods: 105
Gross salary:2,125
"""

def flat_list(nested_list):
    single_list = nested_list[0]
    return single_list

# print(flat_list([[2,4,5,6]]))

def your_salary():
    teacher_name =input("What is the name of teacher? \n")
    number_of_periods =int(input("Please enter number of periods taught in a month \n"))

    if 0 < number_of_periods < 100:
        gross_salary = number_of_periods * 20
    elif 0 < number_of_periods > 100:
        gross_salary = 2000 + (number_of_periods -100) * 25
    
    payslip = f"Teacher: {teacher_name}, \nPeriods: {number_of_periods} \nGross salary: {gross_salary:,}$"
    return payslip

print(your_salary())