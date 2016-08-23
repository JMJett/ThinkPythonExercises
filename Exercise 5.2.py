__author__ = 'Jarod Jett'

def is_triangle(a,b,c):
    if (a + b < c) or (a + c < b) or (c + b < a):
        print("You cannot form a triangle with these lengths.")
    else:
        print("These lengths form a triangle!")

a  = float(input("Enter the first length: "))
b  = float(input("Enter the second length: "))
c  = float(input("Enter the third length: "))

print(a,b,c)

is_triangle(a,b,c)

