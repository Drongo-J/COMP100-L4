"""
# Task 1
# Get the Original Price from the User
original_price = float(input("Enter original price : "))

# Apply 20% discount
sale = 0.8

# Calculate Sale Price
sale_price = original_price * sale

# Print Sale Price
print("Sale Price : ", format(sale_price, ".2f"))
"""

"""
# Task 2

# Getting 3 inputs all together
# x, y, z = input("Enter 3 numbers: ").split()

# Get Score 1
num1 = int(input("Enter Score 1: "))
# Get Score 2
num2 = int(input("Enter Score 2: "))
# Get Score 1
num3 = int(input("Enter Score 3: "))

# Calculate Average
average = (num1 + num2 + num3) / 3

# Print Average
print("Average: ", int(average))
"""


# Task 3

# annual_interest = float(input("Enter annual interest: "))
interest_rate = float(input("Enter interest rate: "))

F = 10000
n = 10

P = F / ((1 + interest_rate) ** n)
print("Present value: ", P)