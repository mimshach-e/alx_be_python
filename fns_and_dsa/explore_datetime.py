# Task 2 - Explore `datetime` Module

from datetime import timedelta, datetime, tzinfo, timezone

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time and save
    current_date = datetime.now()
    
    # Format the current date and time
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the current date and time
    print("Current Date and Time:", formatted_datetime)

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        # Prompt the user to enter a number of days
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        
        # Get the current date
        current_date = datetime.now().date()
        
        # Calculate the future date
        future_date = current_date + timedelta(days=number_of_days)
        
        # Print the future date
        print("Future Date:", future_date)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    # Part 1: Display the Current Date and Time
    display_current_datetime()
    
    # Part 2: Calculate a Future Date
    calculate_future_date()
