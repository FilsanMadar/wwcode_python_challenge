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

