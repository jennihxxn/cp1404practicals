from unreliable_car import UnreliableCar

def main():
    # Create a new UnreliableCar object with 50% reliability
    unreliable_car = UnreliableCar("Unreliable", 100, 50)

    # Try to drive the car 10 times and print the results
    for i in range(10):
        distance_driven = unreliable_car.drive(10)
        print(f"Attempt {i + 1}: Drove {distance_driven} km")

    # Print the car's details after driving attempts
    print(unreliable_car)

if __name__ == "__main__":
    main()
