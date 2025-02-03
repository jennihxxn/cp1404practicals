"""
Temperature Converter Program
"""

def main():
    """Get user input for temperature and conversion type, convert and print the result."""
    temperature = float(input("Enter the temperature: "))
    conversion_type = input("Convert from (C)elsius or (F)ahrenheit? ").upper()

    if conversion_type == "C":
        celsius_temp = temperature
        fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
        print(f"{celsius_temp} degrees Celsius is equal to {fahrenheit_temp} degrees Fahrenheit.")
    elif conversion_type == "F":
        fahrenheit_temp = temperature
        celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
        print(f"{fahrenheit_temp} degrees Fahrenheit is equal to {celsius_temp} degrees Celsius.")
    else:
        print("Invalid conversion type.")

def celsius_to_fahrenheit(celsius_temp):
    """Convert Celsius temperature to Fahrenheit."""
    fahrenheit_temp = (celsius_temp * 9 / 5) + 32
    return fahrenheit_temp

def fahrenheit_to_celsius(fahrenheit_temp):
    """Convert Fahrenheit temperature to Celsius."""
    celsius_temp = (fahrenheit_temp - 32) * 5 / 9
    return celsius_temp

main()