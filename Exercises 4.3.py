__author__ = 'Jarod Jett'

import turtle

def square(t,x):
    for i in range(4):
        t.fd(x)
        t.lt(90)

def polygon(t,x,s):
    for i in range(s):
        t.fd(x)
        t.lt(360/s)

bob = turtle.Turtle()

print(bob)
square(bob,50)
polygon(bob,100,8)

turtle.mainloop()

