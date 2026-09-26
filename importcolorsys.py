import turtle
import colorsys

t = turtle.Turtle()
screen = turtle.Screen()

turtle.tracer(10)
screen.bgcolor("black")

h = 0

for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        t.color(c)
        h += 0.005

        t.right(90)
        t.circle(150 - j * 6, 90)

        t.left(90)
        t.circle(150 - j * 6, 90)

        t.right(180)
        t.circle(40, 24)

turtle.done()