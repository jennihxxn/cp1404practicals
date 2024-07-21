import csv
from guitar import Guitar

FILENAME = 'guitars.csv'

def main():
    """Read guitars from file, display them, add new ones, save to file."""
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted by year (oldest to newest):")
    display_guitars(guitars)

    guitars.extend(get_new_guitars())
    save_guitars(FILENAME, guitars)

def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    """Display a list of guitars."""
    for guitar in guitars:
        print(guitar)

def get_new_guitars():
    """Get new guitars from the user."""
    new_guitars = []
    print("\nEnter new guitars (leave name empty to finish):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitars.append(Guitar(name, year, cost))
    return new_guitars

def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

if __name__ == '__main__':
    main()
