# Day 1 : Create a program that swaps the values of two variables.

# This script takes two variable values as input
# and displays the input values for those variables.

def swap_variable():
    try:
        variable1 = input("Enter the value of your first variable: ")
        variable2 = input("Enter the value of your second variable: ")

        temp_variable = variable1
        variable1 = variable2
        variable2 = temp_variable

        print("\nThese are your variables after the swap: ")
        print("Variable 1: " + variable1)
        print("Variable 2: " + variable2)

    except ValueError:
        print("Please input numerical variable")

# to prevent an error
swap_variable()


