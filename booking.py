# booking.py

from data import bookings
from utils import generate_pnr


def review_booking(passenger_name, flight, travel_date):

    print("\n" + "=" * 60)
    print("                 REVIEW YOUR BOOKING")
    print("=" * 60)

    print("\nPassenger Name :", passenger_name)
    print("Flight Number  :", flight["flight_no"])
    print("Route          :", flight["departure"], "→", flight["arrival"])
    print("Travel Date    :", travel_date)
    print("Departure Time :", flight["time"])
    print("Amount Payable : ₹", flight["fare"])

    print("\n" + "-" * 60)
    print("1. Proceed to Payment")
    print("2. Change Passenger Name")
    print("3. Cancel Booking")
    print("-" * 60)

    return input("\nEnter Choice : ")


def book_ticket(passenger_name, flight, travel_date):

    pnr = generate_pnr()

    booking = {
        "pnr": pnr,
        "name": passenger_name,
        "flight_no": flight["flight_no"],
        "departure": flight["departure"],
        "arrival": flight["arrival"],
        "date": travel_date,
        "time": flight["time"],
        "fare": flight["fare"]
    }

    bookings.append(booking)

    print("\nGenerating your ticket...")
    print("Please wait...")

    print("\n" + "=" * 60)
    print("                     E - TICKET")
    print("=" * 60)

    print("\nPassenger Name :", booking["name"])
    print("PNR            :", booking["pnr"])
    print("Flight Number  :", booking["flight_no"])

    print("\nFrom           :", booking["departure"])
    print("To             :", booking["arrival"])

    print("Travel Date    :", booking["date"])
    print("Departure Time :", booking["time"])

    print("Fare Paid      : ₹", booking["fare"])

    print("Status         : Confirmed ✅")

    print("\nThank You For Choosing Akasa Airlines.")
    print("Have a Pleasant Journey! ✈️")


def view_ticket():

    if not bookings:

        print("\n😔 Sorry Buddy!")
        print("You haven't booked any flights yet.")
        print("Go to Search Flight to book your journey.")

        input("\nPress Enter to continue...")
        return

    print("\n" + "=" * 60)
    print("                  YOUR BOOKED TICKETS")
    print("=" * 60)

    for booking in bookings:

        print("\nPassenger Name :", booking["name"])
        print("PNR            :", booking["pnr"])
        print("Flight Number  :", booking["flight_no"])

        print("From           :", booking["departure"])
        print("To             :", booking["arrival"])

        print("Travel Date    :", booking["date"])
        print("Departure Time :", booking["time"])

        print("Fare Paid      : ₹", booking["fare"])
        print("Status         : Confirmed ✅")

        print("-" * 60)

    input("\nPress Enter to return to Main Menu...")


def cancel_ticket():

    if not bookings:

        print("\n😔 Sorry Buddy!")
        print("No booked tickets found.")

        input("\nPress Enter to continue...")
        return

    print("\nEnter your PNR Number")
    print("Example : AK12345")

    pnr = input("\nPNR : ").strip().upper()

    for booking in bookings:

        if booking["pnr"].upper() == pnr:

            bookings.remove(booking)

            print("\n✅ Ticket Cancelled Successfully.")
            print("We hope to serve you again soon!")

            input("\nPress Enter to return to Main Menu...")
            return

    print("\n❌ Invalid PNR Number.")
    input("\nPress Enter to continue...")