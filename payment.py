# payment.py

def process_payment():

    print("\n" + "=" * 60)
    print("                  PAYMENT GATEWAY")
    print("=" * 60)

    print("\nChoose Your Payment Method")
    print("--------------------------")
    print("1. UPI")
    print("2. CARD")

    # Payment Method Validation
    while True:

        choice = input("\nEnter Choice (1 or 2) : ")

        if choice in ["1", "2"]:
            break

        print("\n❌ Invalid Choice.")
        print("Please enter 1 for UPI or 2 for CARD.")

    # -----------------------
    # UPI PAYMENT
    # -----------------------

    if choice == "1":

        print("\nUPI Payment")
        print("-----------")
        print("Examples:")
        print("rahul@paytm")
        


        while True:

            upi = input("\nEnter UPI ID : ").strip()

            if "@" in upi and len(upi) >= 5:
                break

            print("\n❌ Invalid UPI ID.")
            print("Please enter a valid UPI ID.")
            print("Example : murari@paytm")

    # -----------------------
    # CARD PAYMENT
    # -----------------------

    else:

        print("\nCard Payment")
        print("------------")
        print("Card Number should contain exactly 16 digits.")
        print("Example : 1234567812345678")

        while True:

            card_no = input("\nEnter Card Number : ").strip()

            if len(card_no) == 16 and card_no.isdigit():
                break

            print("\n❌ Invalid Card Number.")
            print("Card Number must contain exactly 16 digits.")

        while True:

            holder = input("\nEnter Card Holder Name : ").strip()

            if holder:
                break

            print("\n❌ Card Holder Name cannot be empty.")

        print("\nCVV should contain exactly 3 digits.")

        while True:

            cvv = input("Enter CVV : ").strip()

            if len(cvv) == 3 and cvv.isdigit():
                break

            print("\n❌ Invalid CVV.")
            print("CVV must contain exactly 3 digits.")

    # -----------------------
    # PAYMENT SUCCESS
    # -----------------------

    print("\nProcessing your payment...")
    print("Please wait...\n")

    print("✅ Payment Successful!")

    return True