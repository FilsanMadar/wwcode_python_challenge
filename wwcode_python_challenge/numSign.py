# Day 7 : write a program to check if a number is positive, negative, or zero

def returnSign(num):

    if num == 0:
        return "Zero"
    elif num < 0:
        return "Negative"
    return "Positive"

num = float(input("Enter a number: "))
print(returnSign(num))

# Day 9 : Write a program to check if a number is even or odd

def even_and_odd():

    inputNum = int(input("Enter your numerical value: "))

    if (inputNum % 2) == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

even_and_odd()