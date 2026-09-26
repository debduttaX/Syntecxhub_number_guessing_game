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
    h += 0.005

    t.forward(i * 2)
    t.right(59)   # magic angle 😏

turtle.done()