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

