# Day 23: Write a program that checks if a key exists in a dictionary.

fruit_dictionary = {"apple": 2,
    "banana": 5,
    "orange": 3,
    "grape": 7,
    "watermelon": 1,
    "pineapple": 4,
    "kiwi": 6,
    "mango": 8,
    "pear": 9,
    "strawberry": 10}

def check_key_existence(key, dictionary):

    if key in dictionary:
        print(f"The key '{key}' exists in the dictionary.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")

key_to_check= input("Enter the key to check: ")
check_key_existence(key_to_check, fruit_dictionary)