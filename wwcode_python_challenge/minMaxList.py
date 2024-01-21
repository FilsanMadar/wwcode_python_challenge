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
