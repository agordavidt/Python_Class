"""
A store is offering a promotional discount. Customers receive a 10% discount on purchases totaling 500 Naira or less,
a 15% discount on purchases between 501 and 999 Naira, and a 20% discount on purchases of 1000 Naira or more. 
Write a program that calculates and prints the final amount a customer will pay based on the total value of 
their purchase.
"""

price_goods = int(input("Enter the Price: "))
discount_1 = price_goods * 0.1
discount_2 = price_goods * 0.15
discount_3 = price_goods * 0.2

if price_goods <= 500:
    pay_amount = price_goods - discount_1
elif price_goods > 500 and price_goods < 1000:
    pay_amount = price_goods - discount_2
else:
    pay_amount = price_goods - discount_3
print("you are to pay: ", pay_amount)

