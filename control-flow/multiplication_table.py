# Multiplication Table Generator

# Prompting User for a Number:
number = int(input("Enter a number to see its multiplication table: "))

# Generating and Printing the Multiplication Table:
for s in range(1, 10 +1):
    product = number * s
    print(f"{number} * {s} = {product}")