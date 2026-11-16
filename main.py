from myFunctions import *
bob.speed(0)
turtle.bgcolor("Sky Blue")
bob.color("yellow")



# spiral design using comet() & jump()
for times in range(36):
    jump(0,0)
    comet(50,40)
    bob.left(30)

bob.color("green")
#Example 3
jump(0,-100)
bob.right(90)
bob.forward(250)

import turtle
bob = turtle.Turtle()
bob.speed(6)
bob.shape("arrow")


