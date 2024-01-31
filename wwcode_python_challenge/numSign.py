# Day 7 : write a program to check if a number is positive, negative, or zero
import math


def returnSign(num):

    if num == 0:
        return "Zero"
    elif num < 0:
        return "Negative"
    return "Positive"

num = float(input("Enter a number: "))
print(returnSign(num))

# Day 9 : Write a program to check if a number is even or odd

def even_and_odd():

    inputNum = int(input("Enter your numerical value: "))

    if (inputNum % 2) == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

even_and_odd()

# Day 19: Write a function to calculate the factorial of a number.

def factoral_number():

    num = int(input("Enter a non negative integer to get factorial of number: "))

    print(math.factorial(num))

factoral_number()

# Day 21: Create a program to remove a specific element from a set.

def remove_element():

    given_input = set(input("Enter set elements: ").split(" "))

    delete_elements = input("Enter the element you want to remove from the set: ")

    given_input.remove(delete_elements)

    print("Updated set = ", given_input)

remove_element()

