#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line:

def bandName():

    print("Hello! I would love to help you create your own custom band name!")
    city = input("What city did you grow up in? \n")
    petName = input("What is your pet name? \n")

    name = str(city + " " + petName)

    print("Your new custom band name is: " + name)

bandName()