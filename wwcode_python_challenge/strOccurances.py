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


# Day 12 : Write a program to reverse a given string.

def reverse_string(input_str):
    return input_str[::-1]


# Take user input
original_str = input("Enter a string: ")

# Reverse the string
reversed_str = reverse_string(original_str)

# print
print("Original String:", original_str)
print("Reversed String:", reversed_str)
