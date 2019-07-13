

import turtle
import random
wn = turtle.Screen()
rafi = turtle.Turtle()
rafi.speed(2)
rafi.shape('turtle')

for i in range(0, 100):
    for aColor in ["yellow", "red", "purple", "dark blue", 'black', 'dark orange', 'brown']:
        rafi.color(aColor)
        rafi.goto((random.randrange(-100, 100)), (random.randrange(-100, 100)))
        rafi.goto(0, 0)

wn.exitonclick()




