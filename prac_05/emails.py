"""
CP1404/CP5632 Practical
"""
def extract_name(email):
    parts = email.split('@')[0].split('.')
    return ' '.join(part.title() for part in parts)

def main():
    email_to_name = {}

    while True:
        email = input("Email: ").strip()
        if not email:
            break

        name = extract_name(email)
        response = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if response and response != 'y':
            name = input("Name: ")

        email_to_name[email] = name

    print("\nStored emails and names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()