# Day 15 : Create a program that checks if a year is a leap year.

def check_leap_year(given_year):

    if (given_year % 100 == 0) and (given_year % 400 != 0):
        return False

    elif given_year % 4 != 0:
        return False
    else:
        return True


given_year = int(input("Please enter the year you want to check: "))

print(check_leap_year(given_year))

