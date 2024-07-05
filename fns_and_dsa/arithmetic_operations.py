# Functions, Data Structures and Modules 
# Task 0 - Arithmetic Operations Function

# Variable Declaration
num1 = float(0)
num2 = float(0)
operation = str("")

# Function Definition
def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Division by zero is not allowed!"
        else:
            return num1 / num2
            
    else:
        print("Operation not found!")

       


