# flights.py

from datetime import datetime, timedelta
from data import flights


def search_flight():

    print("\n" + "=" * 60)
    print("                   SEARCH FLIGHTS")
    print("=" * 60)

    print("\nEnter Departure and Arrival Cities")
    print("----------------------------------")
    print("Example:")
    print("Departure : Hyderabad")
    print("Arrival   : Mumbai")

    # -------------------------------
    # Departure & Arrival Validation
    # -------------------------------
    while True:

        departure = input("\nDeparture City : ").strip().lower()
        arrival = input("Arrival City   : ").strip().lower()

        if departure == arrival:

            print("\n❌ Departure and Arrival cannot be the same.")
            print("Please enter different cities.")

        else:
            break

    # -------------------------------
    # Travel Date Validation
    # -------------------------------
    while True:

        print("\nEnter Travel Date (DD-MM-YYYY)")
        print("Example : 07-07-2026")

        date_input = input("Date : ")

        try:

            travel_date = datetime.strptime(
                date_input,
                "%d-%m-%Y"
            ).date()

            today = datetime.today().date()

            if travel_date < today:

                print("\n❌ Travel date cannot be in the past.")
                print("Please enter a future date.")
                continue

            if travel_date > today + timedelta(days=2):

                print("\n❌ No Flights Available.")
                print("Flights can only be booked")
                print("for Today, Tomorrow or the Next Day.")
                continue

            break

        except:

            print("\n❌ Invalid Date Format.")
            print("Please enter the date in DD-MM-YYYY format.")
            print("Example : 07-07-2026")

    # -------------------------------
    # Search Flights
    # -------------------------------

    available = []

    for flight in flights:

        if (
            flight["departure"].lower() == departure
            and
            flight["arrival"].lower() == arrival
        ):

            available.append(flight)

    if not available:

        print("\n❌ No Flights Found.")
        print("Please try another route.")

        return None, None

    # -------------------------------
    # Display Flights
    # -------------------------------

    print("\n" + "=" * 60)
    print("                AVAILABLE FLIGHTS")
    print("=" * 60)

    for i, flight in enumerate(available, start=1):

        print(f"\nFlight {i}")
        print("-" * 30)
        print("Flight Number :", flight["flight_no"])
        print("Route         :", flight["departure"], "→", flight["arrival"])
        print("Departure Time:", flight["time"])
        print("Ticket Fare   : ₹", flight["fare"])

    print("\n--------------------------------------------")
    print("Select a Flight by entering its number.")
    print("--------------------------------------------")

    while True:

        try:

            choice = int(input("Choice : "))

            if 1 <= choice <= len(available):
                break

            print("\n❌ Invalid Flight Number.")
            print("Please select a valid option.")

        except:

            print("\n❌ Please enter numbers only.")

    return available[choice - 1], travel_date