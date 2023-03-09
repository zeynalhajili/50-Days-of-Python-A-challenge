"""
Day 5: My Discount
Create a function called my_discount. The function takes no arguments but asks the
user to input the price and the discount (percentage) of the product. Once the user
inputs the price and discount, it calculates the price after the discount. The 
function should return the price after the discount. For example, if the user 
enters 150 as price and 15% as the discount, your function should return 127.5.
"""

def my_discount():
    
    price_input= int(input("Please enter the price: "))
    discount_input=int(input("Please enter the discount: "))
    return f'Final price will be {price_input*(100-discount_input)/100:.1f} dollar after {discount_input} % discount!!'

print(my_discount())
