# Drawing Patterns with Nested Loops

# Prompting User for Pattern Size:
size_of_pattern = int(input("Enter the size of the pattern: "))

# Initializing the row counter
row = 0

# Drawing the Pattern:
while row < size_of_pattern:
    for i in range(size_of_pattern):
        print("*", end="")
    print()
    row += 1
