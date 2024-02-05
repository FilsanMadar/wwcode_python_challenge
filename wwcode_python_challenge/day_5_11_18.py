# Day 5 : Write a program to find the maximum and minimum values in a list.

def minAndMax():
    # user enters list numbers
    inputNumList = input("Enter your numerical values: ")
    # changed to list by .split
    numList = [int(num) for num in inputNumList.split()]
    # min numbers
    minOfNum = min(numList)
    # max numbers
    maxOfNum = max(numList)
    # change numbers back to str and print
    print("Here is the minimum values of the list: " + str(minOfNum))
    print("Here is the maxium values of the list: " + str(maxOfNum))


minAndMax()


# Day 11 : Write a program to print the multiplication table of a given number.

def multiplication_table():
    given_number = int(input("Enter your number: "))
    # iterate 10 times from i = 1 to 11
    for i in range(1, 11):
        print(given_number, "x", i, "=", given_number * i)


multiplication_table()

# Day 18: Create a program to find the largest among three numbers.

def max_number():
    numbers = []  # Create an empty list to store numbers

    # Prompt the user to enter 3 numbers separated by spaces
    given_numbers = input("Enter 3 numbers separated by spaces: ")

    # Split the input string into individual numbers and convert them to integers
    numbers = [int(num) for num in given_numbers.split()]

    # Check if the user has entered exactly 3 numbers
    if len(numbers) != 3:
        print("Please enter exactly 3 numbers.")
        return  # Exit the function if the user input is invalid

    # Find the largest number using the max() function
    max_num = max(numbers)

    # Print the result
    print("Largest number:", max_num)

# Call the function to find the largest number among three numbers
max_number()




