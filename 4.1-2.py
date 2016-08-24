__author__ = 'Jarod Jett'

import turtle

bob = turtle.Turtle()

print(bob)

bob.fd(100)

for i in range(3):
    bob.lt(90)
    bob.fd(100)

turtle.mainloop()

