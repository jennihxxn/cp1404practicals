"""
Password Stars Program
"""

# Define the minimum password length
MIN_PASSWORD_LENGTH = 8

def main():
    """Get a password from the user and print asterisks with the same length."""
    password = get_password()
    print_asterisks(password)

def get_password():
    """Get a valid password from the user."""
    password = input("Enter a password: ")
    while len(password) < MIN_PASSWORD_LENGTH:
        print(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password

def print_asterisks(password):
    """Print asterisks with the same length as the provided password."""
    print("*" * len(password))

main()