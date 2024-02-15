# Day 36: Write a Python program to check if two strings are anagrams

def check_anagram():
    given_input1 = input("Enter your first input: ")
    given_input2 = input("Enter your second input: ")

    # change the string to all lower case
    given_input1 = given_input1.lower()
    given_input2 = given_input2.lower()

    # check to make sure the length of characters are the same.
    if len(given_input1) == len(given_input2):

        # sorts both of the strings
        sorted_str1 = sorted(given_input1)
        sorted_str2 = sorted(given_input2)

        # checks to make sure they are equal
        if sorted_str1 == sorted_str2:
            print(given_input1 + " and " + given_input2 + " are anagrams.")
        else:
            print(given_input1 + " and " + given_input2 + " are not anagrams.")
    else:
        print(given_input1 + " and " + given_input2 + " are not anagrams.")


check_anagram()
