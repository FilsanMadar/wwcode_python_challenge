# Day 7 : write a program to check if a number is positive, negative, or zero

def returnSign(num):

    if num == 0:
        return "Zero"
    elif num < 0:
        return "Negative"
    return "Positive"

num = float(input("Enter a number: "))
print(returnSign(num))