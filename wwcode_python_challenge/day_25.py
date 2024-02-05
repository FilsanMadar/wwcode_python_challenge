# Day 25 : Create a program to concatenate two lists.

def concat_list():

    input_one = input("Enter input here: ").split()
    input_two = input("Enter input here: ").split()

    concat_inputs = input_one + input_two

    print("Here are your concatenated lists: ", concat_inputs)

concat_list()