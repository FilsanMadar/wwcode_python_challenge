# Day 1 : Create a program that swaps the values of two variables.

# This script takes two variable values as input
# and displays the input values for those variables.

variable1 = input("Enter the value of your first variable: ")
variable2 = input("Enter the value of your second variable: ")

tempVariable = variable1
variable1 = variable2
variable2 = tempVariable

print("\nThese are your variables after the swap: ")
print("Variable 1: " + variable1)
print("Variable 2: " + variable2)