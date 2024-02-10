# Day 29: Create a function that generates a random number between a given range.
import random


def generate_random():

    a_input = int(input("Enter your first number in your range: "))
    b_input = int(input("Enter your second number in your range: "))

    random_num = random.randint(a_input, b_input)

    print("Your random number is: ", random_num)

generate_random()