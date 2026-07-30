# Flight-Booking-System
Flight Booking System developed using Python without SQL database
# Flight Booking System

## Project Description

The Flight Booking System is a Python-based application developed to simulate a real-world flight reservation system. The main objective of this project is to provide users with functionalities such as user registration, login, searching available flights, booking tickets, viewing booking details, and cancelling reservations.

The project is developed using Python programming concepts without using a database. Data is managed using Python data structures such as lists and dictionaries, and persistent storage is implemented using JSON files.

## Features Implemented

### 1. User Registration and Login

* Users can create an account and log in to the system.
* User credentials are stored securely using JSON file handling.
* Only registered users can access booking features.

### 2. Flight Management

* The system maintains available flight details such as:

  * Flight ID
  * Airline name
  * Source location
  * Destination location
  * Ticket price
  * Available seats

### 3. Search Flights

* Users can search flights based on:

  * Source location
  * Destination location
* The system displays matching available flights.

### 4. Ticket Booking

* Users can book tickets by selecting a flight.
* The system checks seat availability before confirming the booking.
* After successful booking:

  * Booking details are generated.
  * Available seats are updated automatically.
  * Total ticket amount is calculated.

### 5. View Booking Details

* Users can view their booking information including:

  * Booking ID
  * Passenger name
  * Flight details
  * Number of seats booked
  * Total amount

### 6. Cancel Booking

* Users can cancel their existing bookings.
* The system removes the booking record and updates available seats.

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* File Handling
* JSON Data Storage
* Exception Handling

## Concepts Applied

* Classes and Objects
* Functions
* Lists and Dictionaries
* Conditional Statements
* Loops
* Modular Programming
* Data Persistence using JSON files

## Project Objective

The objective of this project is to understand how real-world booking systems work by implementing user management, availability checking, reservation processing, and data handling using Python programming techniques.
