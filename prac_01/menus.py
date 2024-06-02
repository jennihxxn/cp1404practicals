"""
Pseudocode for menus

    GET a name from user
    Create menu options

    Repeat until choice is not "Q":
        Print "(H)ello"
        Print "(G)oodbye"
        Print "(Q)uit"
        GET input and convert to uppercase

        If choice is "H":
            Print "Hello" name
        Else if choice is "G":
            Print "Goodbye" name
        Else if choice is "Q":
            Print "Finished."
        Else:
            Print "Invalid choice"
"""

name = input("Enter name: ")

menu_options = {
    "H": "(H)ello",
    "G": "(G)oodbye",
    "Q": "(Q)uit" }
choice = ""
while choice != "Q":
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>>").upper()

    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    elif choice == "Q":
        print("Finished.")
    else:
        print("Invalid choice")
