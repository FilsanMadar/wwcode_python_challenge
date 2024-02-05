# Day 2 - Create a program to calculate the area of a circle given its radius.

def areaOfCircle():
    radius = int(input("Enter the radius of the circle: "))
    pi = 3.14

    circle_area = pi * radius**2
    print(f"The area of the circle is: + {circle_area}")

areaOfCircle()
