"""
Score Menu Program
"""

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100

def main():
    """Get a valid score and display a menu for score-related operations."""
    score = get_valid_score()
    print(f"Your initial score is: {score}")

    menu_choice = ""
    while menu_choice != "Q":
        print_menu()
        menu_choice = input(">>> ").upper()
        if menu_choice == "G":
            score = get_valid_score()
            print(f"Your new score is: {score}")
        elif menu_choice == "P":
            result = determine_result(score)
            print(result)
        elif menu_choice == "S":
            print_stars(score)
        elif menu_choice != "Q":
            print("Invalid menu choice")

    print("Farewell!")

def print_menu():
    """Print the menu of options."""
    print("""
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit""")

def get_valid_score():
    """Get a valid score (between 0 and 100) from the user."""
    score = int(input("Enter a score between 0 and 100: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = int(input("Enter a score between 0 and 100: "))
    return score

def determine_result(score):
    """Determine the result based on the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    """Print stars based on the given score."""
    print("*" * score)

main()