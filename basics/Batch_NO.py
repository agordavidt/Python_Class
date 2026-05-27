"""
Let’s say your company has a product with this batch number: “037-0091-00027.
first 3 digit is the country code,
 next 4 digit is the product code and the last 5 digit is the batch number.
Create a program to print
Country code…
Product code…
Batch number….

"""
batch_number = "037-0091-00027"
print("The country code is ", batch_number[:3])
print("The product code is ", batch_number[4:8])
print("The batch number is ", batch_number[9:])