from musician import Musician
from guitar import Guitar

def main():
    # Create some guitars
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Line 6 JTV-59", 2010, 1512.9)

    # Create a musician and add guitars to their list of instruments
    musician = Musician("John")
    musician.add_instrument(guitar1)
    musician.add_instrument(guitar2)

    # Print the musician's details
    print(musician)

    # Assert the musician's instruments
    assert len(musician.instruments) == 2
    assert str(musician.instruments[0]) == "Gibson L-5 CES (1922) : $16035.40"
    assert str(musician.instruments[1]) == "Line 6 JTV-59 (2010) : $1512.90"

if __name__ == "__main__":
    main()
