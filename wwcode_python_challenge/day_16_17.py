#Day 16: Write a function that counts the frequency of each word in a sentence.

def count_word_frequency(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Create an empty dictionary to store word frequencies
    word_frequency = {}

    # Iterate through each word in the list of words
    for word in words:
        # Check if the word is already in the dictionary
        if word in word_frequency:
            # If the word is already in the dictionary, increment its count
            word_frequency[word] += 1
        else:
            # If the word is not in the dictionary, add it with count 1
            word_frequency[word] = 1

    return word_frequency

# Example usage:
sentence = input("Enter a sentence: ")
frequency = count_word_frequency(sentence)

print("Word frequency in the sentence:")
for word, count in frequency.items():
    print(f"{word}: {count}")


# Day 17 : Create a program that capitalizes the first letter of each word in a sentence

def capitalize_letter(sentence):

    words = sentence.split()

# Capitalize the first letter of each word and join them back into a sentence
    capitalized_sentence = " ".join(word.capitalize() for word in words)

    return capitalized_sentence

sentence = input("Enter a sentence: ")
capitalized_sentence = capitalize_letter(sentence)

print("Capitalized sentence: " + capitalized_sentence)
