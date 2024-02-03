# Day 22 : Create a program to find the second-largest element in a list.

def second_max_list():
# get a list of numbers
    given_numbers = input("Enter list of numbers: ").split()

    given_numbers = [int(num) for num in given_numbers]
# determine the max value of a given list
    max_value = max(given_numbers)
# remove the max value from the list
    given_numbers.remove(max_value)
# determine the new max value
    max_value2 = max(given_numbers)

    print("The second largest element is: ", max_value2)

second_max_list()