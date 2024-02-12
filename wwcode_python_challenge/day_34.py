# Day 34: Write a Python program to merge two dictionaries

first_dict = {"Germany": "Berlin",
              "Canada": "Ottawa",
              "England": "London"}

second_dict = {"United States": "New York",
               "Italy": "Rome"}


def combine_dict():
    first_dict.update(second_dict)  # used the update() to add the data in the second_dict

    print(first_dict)


combine_dict()
