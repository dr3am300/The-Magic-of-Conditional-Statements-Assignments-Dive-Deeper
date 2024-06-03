# Objective:
# Dive deep into the intricacies of the calendar by exploring the concept of leap years.
# Task 1: Leap Year Checker----------------------------------
# Write a Python program that prompts the user to input a year. 
# The program should determine if the given year is a leap year or not and then display an appropriate message. 
# Please note that this is the definition of a leap year: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

is_leap_year = int(input("Enter a year: "))
if is_leap_year % 4 == 0:
    print(f"{is_leap_year} This is True, is a leap year.")
elif is_leap_year % 100 == 0:
    print(f"{is_leap_year} this is False, is not a leap year.")
elif is_leap_year % 400 == 0:
    print(f"{is_leap_year} This is True, is a leap year.")
else:
    print(f"{is_leap_year} This is False, is not a leap year.")

# A more simplified version of the code above

is_leap_year = int(input("Enter a year: "))

if (is_leap_year % 4 == 0 or is_leap_year % 100 != 0 and is_leap_year % 400 == 0):
    print(f"{is_leap_year} This is True, is a leap year.")
else:
    print(f"{is_leap_year} This is False, is not a leap year.")
    