# Day 32 : Create a function that calculates the average of a list of numbers
import statistics

def avg_numbers():

    given_input = input("Enter your list of numbers: ")

    numList = [int(num) for num in given_input.split()]

    average = statistics.mean(numList)

    print("The average of this list of numbers is:  ", average)

avg_numbers()



