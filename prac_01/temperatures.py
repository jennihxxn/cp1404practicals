"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

DEFINE MENU as a string containing the menu options
PRINT the MENU

GET user choice
WHILE choice is not "Q"
   IF choice is "C"
       GET Celsius value from the user
       calculate Fahrenheit value using the formula: fahrenheit = celsius * (9.0 / 5) + 32
       PRINT result "Result: {fahrenheit:.2f} F"
   ELSE IF choice is "F"
       GET Fahrenheit value from the user
       calculate Celsius value using the formula: celsius = (fahrenheit - 32) * (5 / 9)
       PRINT result "Result: {celsius:.2f} C"
   ELSE
       PRINT "Invalid option"
   PRINT MENU
   GET the user choice again
PRINT "Thank you."
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")