"""
Day 19: Words and Elements
Write two functions. The first function is called count_words which takes a string of 
words and counts how many words are in the string.
The second function called count_elements takes a string of words and counts how many
elements are in the string. Do not count the whitespaces. The first function will 
return the number of words in a string and the second one will return the number of 
elements (less whitespace). If you pass ‘I love learning’, the count_words function 
should return 3 words and count_elements should return 13 elements.
"""

def count_words(input_string):
    count = 0
    string_to_list = input_string.split(" ")
    for i in string_to_list:
        count = count + 1
    return count

def count_elements(input_string):
    stringx = "".join(input_string.split(" "))
    return len(stringx)

print(count_words("CloudFormation is a powerful automation service within AWS. It can be used to create simple or complex sets of infrastructure any number of times. This hands-on lab provides a gentle introduction to CloudFormation, using it to create and update a number of S3 buckets. By the end of this hands-on lab, you will be comfortable using CloudFormation and can begin experimenting with your own templates."))
print(count_elements("CloudFormation is a powerful automation service within AWS. It can be used to create simple or complex sets of infrastructure any number of times. This hands-on lab provides a gentle introduction to CloudFormation, using it to create and update a number of S3 buckets. By the end of this hands-on lab, you will be comfortable using CloudFormation and can begin experimenting with your own templates."))
print(count_words('I love learning'))
print(count_elements('I love learning'))
