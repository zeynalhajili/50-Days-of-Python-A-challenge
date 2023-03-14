"""
Day 13: Pay Your Tax
Write a function called your_vat. The function takes no parameter. The function asks 
the user to input the price of an item and VAT (vat should be a percentage). The 
function should return the price of the item plus VAT. If the price is 220 and, VAT 
is 15% your code should return a vat inclusive price of 253. Make sure that your 
code can handle ValueError. Ensure the code runs until valid numbers are entered. 
(hint: Your code should include a while loop).
"""

def your_vat():
    price_of_item = float(input("Please enter price of item: \n"))
    price_vat = float(input("Please enter VAT: \n"))
    while True:
        try:
            if price_of_item < 0 or price_vat < 0:
                raise ValueError
            final_result =(price_of_item*price_vat)/100 + price_of_item
            return f'Final price with VAT is {final_result} $'
            break
        except ValueError:
            return "Please enter correct value!"
print(your_vat())



