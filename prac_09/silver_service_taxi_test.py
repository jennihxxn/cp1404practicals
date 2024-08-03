from silver_service_taxi import SilverServiceTaxi

def main():
    # Create a new SilverServiceTaxi object
    my_silver_taxi = SilverServiceTaxi("Hummer", 200, 2)

    # Drive the SilverServiceTaxi 18 km
    my_silver_taxi.drive(18)

    # Print the SilverServiceTaxi's details and the current fare
    print(my_silver_taxi)
    fare = my_silver_taxi.get_fare()
    print(f"Current fare: ${fare:.2f}")

    # Assert that the fare is as expected ($48.80 for 18 km with fanciness of 2)
    assert abs(fare - 48.80) < 0.01, f"Expected fare to be $48.80, but got {fare:.2f}"

if __name__ == "__main__":
    main()
