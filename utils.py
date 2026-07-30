# utils.py

import random


def generate_pnr():

    return "AK" + str(random.randint(10000, 99999))


def welcome():

    print("\n")
    print("=" * 60)
    print("             ✈️  WELCOME TO AKASA AIRLINES ✈️")
    print("=" * 60)

    print("\n        Fly High, Fly Smart")

    print("\nTravel is the only thing you buy")
    print("that makes you richer.")

    print("\n" + "-" * 60)
    print("Book your journey in just a few simple steps!")
    print("-" * 60)