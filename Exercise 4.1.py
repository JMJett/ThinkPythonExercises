import turtle
bob = turtle.Turtle()
print(bob)

#Make a Square
bob.fd(100)

for i in range(3):
    bob.lt(90)
    bob.fd(100)


turtle.mainloop()
