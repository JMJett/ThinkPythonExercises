__author__ = 'Jarod Jett'

def compare(x,y):
    if (x > y):
        return 1
    else:
        return -1

x = float(input("Enter a value for X: "))
y= float(input("Enter a value for Y: "))

print(compare(x,y))

