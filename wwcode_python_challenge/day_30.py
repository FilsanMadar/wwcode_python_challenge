# Day 30: Create a function that finds the second smallest element in a list.

def second_smallest():

    given_input = input("Enter your list of numbers here: ").split()

    minInput = min(given_input)

    given_input.remove(minInput)

    minInput2 = min(given_input)

    print('The second smallest number is: ', minInput2)

second_smallest()