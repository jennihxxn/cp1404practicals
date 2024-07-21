"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

# Constants
MIN_LENGTH = 5
MAX_LENGTH = 15
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)

    password_is_valid = False
    number_of_days = 0
    while not password_is_valid:
        number_of_days += 1
        password = input(f"> ")
        password_is_valid = is_valid_password(password)

    print(f"Your {len(password)}-character password is valid: {password}")
    print(f"Attempts: {number_of_days}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # Check password length
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        print(f"Invalid password!")
        return False

    # Check for lowercase
    if not any(char.islower() for char in password):
        print("Invalid password!")
        return False

    # Check for uppercase
    if not any(char.isupper() for char in password):
        print("Invalid password!")
        return False

    # Check for digit
    if not any(char.isdigit() for char in password):
        print("Invalid password!")
        return False

    # Check for special characters (if required)
    if IS_SPECIAL_CHARACTER_REQUIRED and not any(char in SPECIAL_CHARACTERS for char in password):
        print("Invalid password!")
        return False

    return True


# Run the program
main()