# Day 33: Write a test case for a function that checks if a number is prime

'''
check if the number is prime or not.
a positive int thats greater than 1 which has no other factors except 1
and the number itself are prime numbers
ex: 2, 3, 5, 7
'''
def is_prime():

    n = int(input("Enter your chosen number: "))

    if n == 1:
        print("This number is not a prime number.")

    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                print("This is not a prime number")
                break
        else:
            print("This is a prime number.")

is_prime()

