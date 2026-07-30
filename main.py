# main.py

from utils import welcome
from flights import search_flight
from payment import process_payment
from booking import (
    review_booking,
    book_ticket,
    view_ticket,
    cancel_ticket
)

while True:

    welcome()

    print("\nMAIN MENU")
    print("-" * 20)
    print("1. Search Flight")
    print("2. View Ticket")
    print("3. Cancel Ticket")
    print("4. Exit")

    choice = input("\nEnter Your Choice : ")

    # ---------------------------------
    # SEARCH FLIGHT
    # ---------------------------------

    if choice == "1":

        flight, travel_date = search_flight()

        if flight:

            while True:

                passenger_name = input(
                    "\nEnter Passenger Name : "
                ).strip()

                if passenger_name:
                    break

                print("\n❌ Passenger Name cannot be empty.")

            while True:

                option = review_booking(
                    passenger_name,
                    flight,
                    travel_date
                )

                if option == "1":

                    if process_payment():

                        book_ticket(
                            passenger_name,
                            flight,
                            travel_date
                        )

                    break

                elif option == "2":

                    while True:

                        passenger_name = input(
                            "\nEnter New Passenger Name : "
                        ).strip()

                        if passenger_name:
                            break

                        print(
                            "\n❌ Passenger Name cannot be empty."
                        )

                elif option == "3":

                    print("\nBooking Cancelled.")
                    break

                else:

                    print("\n❌ Invalid Choice.")
                    print("Please select 1, 2 or 3.")

    # ---------------------------------
    # VIEW TICKET
    # ---------------------------------

    elif choice == "2":

        view_ticket()

    # ---------------------------------
    # CANCEL TICKET
    # ---------------------------------

    elif choice == "3":

        cancel_ticket()

    # ---------------------------------
    # EXIT
    # ---------------------------------

    elif choice == "4":

        print("\n" + "=" * 60)
        print("     Thank You For Choosing Akasa Airlines")
        print("        Have a Safe and Happy Journey!")
        print("            See You Again Soon ✈️")
        print("=" * 60)

        break

    # ---------------------------------
    # INVALID MENU
    # ---------------------------------

    else:

        print("\n❌ Invalid Choice.")
        print("Please select an option between 1 and 4.")