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

def typeLetters(input_string):
    """
        Counts and returns the number of uppercase and lowercase letters in the input string.

        Parameters:
        input_string (str): The string to be analyzed.

        Returns:
        tuple: A tuple containing the counts of uppercase and lowercase letters.
    """
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    return lower_count, upper_count

input_string = str(input("Enter your sentence here to calculate the uppercase and lowercase letters are present: "))
upper_count, lower_count = typeLetters(input_string)

print("The number of uppercase letters is: ", upper_count)
print("The number of lowercase letters is: ", lower_count)

