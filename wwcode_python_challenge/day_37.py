# Day 37 : Write a program to iterate through a dictionary and print its keys and values

def dict():
    first_dict = {"Germany": "Berlin",
                  "Canada": "Ottawa",
                  "England": "London"}

    for key, value in first_dict.items():

        print(f"Key: {key}, Value: {value}")

dict()
