import turtle
import colorsys

t = turtle.Turtle()
screen = turtle.Screen()

t.speed(0)
turtle.bgcolor("black")

h = 0

for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.color(c)
    h += 0.01

    t.left(1)
    t.forward(1)

    for j in range(2):
        t.circle(100 - i, 90)
        t.circle(100 - i, 90)

turtle.done()