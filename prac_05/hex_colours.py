"""
CP1404/CP5632 Practical
"""

COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2"
}

print("Welcome to the Hexadecimal Colour Lookup")
print("Enter a colour name to get its hexadecimal code")
print("Press Enter with no input to quit")

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    try:
        print(f"The hexadecimal code for {colour_name} is {COLOUR_CODES[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").lower()

print("Thank you for using the Hexadecimal Colour Lookup")