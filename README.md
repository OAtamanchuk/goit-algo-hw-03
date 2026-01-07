## Description

This repository contains solutions for Homework 3 of the GoIT Python course.
The project focuses on implementing practical utility functions using core Python features, such as working with dates, random number generation, string processing, and regular expressions.

## Technologies & Stack

The project is implemented using the following technologies:
- Python 3
- Standard Python libraries:
  - datetime - date and time calculations
  - random - random number generation
  - re - regular expressions for string processing
-Basic algorithmic techniques

No external dependencies are required.

## Functionality

The repository includes implementations of the following functions:

1️. get_days_from_today(date)

Calculates the number of days between a given date and the current date.
Accepts a date string in the format YYYY-MM-DD.
Returns a positive or negative integer depending on whether the date is in the past or future.
Ignores time (hours, minutes, seconds).

2️. get_numbers_ticket(min, max, quantity)

Generates a set of unique random numbers within a specified range.
Parameters:
- min - minimum possible number (≥ 1)
- max - maximum possible number (≤ 1000)
- quantity - amount of numbers to generate
  
Returns a sorted list of unique numbers.
Returns an empty list if input parameters are invalid.

3️. normalize_phone(phone_number)

Normalizes phone numbers to a standard international format.
Removes all characters except digits and the + symbol.
Automatically adds the Ukrainian country code +38 if missing.
Supports various input formats (spaces, brackets, dashes, tabs, etc.).
Returns a clean phone number suitable for SMS distribution systems.
