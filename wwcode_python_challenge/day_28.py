# Day 28: Create a program that removes the nth element from a list.

def remove_element():

    given_input = input("Enter list of elements seperated by space: ").split()

    delete_elements = input("Enter the element you want to remove from the set: ")

    given_input.remove(delete_elements)

    print("Updated list = ", given_input)


remove_element()

