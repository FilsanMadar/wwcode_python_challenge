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

# Day 10 : Write a program to remove duplicates from a list.

def remove_duplicate():
    given_num_list = input("Enter a list of numbers: ")
    # convert input string into list
    # use set() to remove duplicate from list
    remove_list = list(set(given_num_list))
    print("The list after removing the duplicates is: " + str(remove_list))

remove_duplicate()


