# Day 3: Write a function to count the number of vowels in a given string

def numVowels():

    givenStrg = str(input("Enter your sentence here to check the number of vowels: "))
    vowel = set("aeiouAEIOU")
    count = 0

    for char in givenStrg:
        if char in vowel:
            count = count + 1
    print("The number of vowels is: " + str(count))

numVowels()

# Day 8 : Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

def typeLetters():

    input_string = str(input("Enter your sentence here to calculate the uppercase and lowercase letters are present: "))
    upper_letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lower_letters = set("abcdefghijklmnopqrstuvwxyz")
    count1 = 0
    count2 = 0

    for char in input_string:
        if char in upper_letters:
            count1 = count1 + 1
        if char in lower_letters:
            count2 = count2 + 1

    print("The number of uppercase letters is: " + str(count1))
    print("The number of lowercase letters is: " + str(count2))

typeLetters()


