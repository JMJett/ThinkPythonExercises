__author__ = 'Jarod Jett'

import turtle
import math

def square(t,x):
    for i in range(4):
        t.fd(x)
        t.lt(90)

def polygon(t,x,s):
    for i in range(s):
        t.fd(x)
        t.lt(360/s)

def circle(t,r):
    c = 2 * math.pi * r
    n = int(c / 3) + 1
    length = c / n
    polygon(t,length,n)

bob = turtle.Turtle()

print(bob)
square(bob,50)
polygon(bob,100,8)
circle(bob,40)

turtle.mainloop()

