# Day 24 : Write a program to remove vowels from a given string.

def remove_vowels():

    given_input = str(input("Enter your sentence here to check the number of vowels: "))
    vowels = set("aeiouAEIOU")

    removed = ''.join(char for char in given_input if char not in vowels)

    print(f"Here is your sentence without vowels: " + removed)

remove_vowels()