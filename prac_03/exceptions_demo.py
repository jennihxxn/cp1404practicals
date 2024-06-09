"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   # If the user inputs a value that can't be turned into a number an error called ValueError will pop up.
   # using the int() function. For example, if the user enters a string like "abc" or a floating-point
   # number like "1.5" instead of an integer.

2. When will a ZeroDivisionError occur?
   # If a user inputs 0 as the denominator it will lead to a ZeroDivisionError in math.
   # division by zero is undefined, and in Python, it raises a ZeroDivisionError.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   # Sure we have the option to update the code to verify if the bottom number is zero prior, to executing the division.
   # If it is zero, we can handle it separately without raising a ZeroDivisionError.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Change to avoid ZeroDivisionError
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")