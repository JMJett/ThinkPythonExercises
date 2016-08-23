__author__ = 'Jarod Jett'
import math

def hypotenuse(a,b):
    squared = a**2 + b**2
    c = math.sqrt(squared)
    return c

a = float(input("Enter side A of the  triangle: "))
b = float(input("Enter side B of the triangle: "))

print("The hypotenuse is ", hypotenuse(a,b))
