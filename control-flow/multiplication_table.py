# Multiplication Table Generator

# Prompting User for a Number:
number = int(input("Enter a number to see its multiplication table: "))

# Generating and Printing the Multiplication Table:
for y in range(1, 11):
    product = number * y
    print(f"{number} * {y} = {product}")