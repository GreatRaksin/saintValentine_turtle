from functions import xt, yt
from turtle import *

t = Turtle()
t.speed(800)

colormode(255)
Screen().bgcolor((0, 0, 0))
for i in range(350):
    t.goto((xt(i) * 20, yt(i) * 20))
    t.pencolor((255 - i) % 255, i % 255, (255 + i) // 2 % 255)
    t.goto(0, 0)

hideturtle()
update()
done()