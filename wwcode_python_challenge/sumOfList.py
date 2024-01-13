# Day 4 : Write a program to find the sum of all elements in a list.

def sumOfList():

# user input list
    inputNumList = input("Enter a list of numbers, to get their sum: ")
# Convert the input string into a list using .split()
    numList = [int(num) for num in inputNumList.split()]
# calculate the sum of the list
    sumofNum = sum(numList)
# convert your list back to a string when your ready to print
    print("The sum of your numbers are: "+ str(sumofNum))

sumOfList()
