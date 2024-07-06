# Define Global Conversion Factors:
FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)

# Implement Conversion Functions:
def convert_to_celsius(fahrenheit):
    temperature_in_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temperature_in_celsius

def convert_to_fahrenheit(celsius):
    temperature_in_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temperature_in_fahrenheit

# User Interaction:
try:
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if unit == "C":
        temperature_in_fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {temperature_in_fahrenheit}°F")

    elif unit == "F":
        temperature_in_celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {temperature_in_celsius}°C")

    else:
       print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


except ValueError as e:
    print(f"Invalid temperature. Please enter a numeric value. Error {e}")