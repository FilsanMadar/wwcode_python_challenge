# Day 6 : Write a program to count the occurrences of a specific character in a string.

def strOccurances():

    inputString = input("Enter a sentence: ")
    target_char = input("Which character do you want to count? ")
    count = 0

    for char in inputString:
        if char == target_char:
            count = count + 1

    print(f"The number of character occurances of {target_char} in {inputString} is: {count}")

strOccurances()


