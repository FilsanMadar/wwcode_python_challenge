# Day 26: Create a program that uses a lambda function to square each element of a list.

given_list = input("Enter your list of numbers: ").split()

# Convert the list of strings to a list of integers
given_list = [int(num) for num in given_list]

# Define the lambda function to square each element
squared = lambda x: x ** 2

# Apply the lambda function to each element of the list and print the result
for num in given_list:
    print(squared(num))