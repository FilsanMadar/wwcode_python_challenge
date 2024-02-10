# Day 31: Create a program that checks if a given string is a valid email address.

def valid_email_address():

    valid_email_domain = ['@gmail.com', '@yahoo.com', '@hotmail.com']

    given_input = input("Please enter a valid email address: ")


    if any(domain in given_input for domain in valid_email_domain):
        print("Your email address is valid")
        return True
    else:
        if given_input not in valid_email_domain:
            print("You have entered an invalid email address")
            return False

valid_email_address()
