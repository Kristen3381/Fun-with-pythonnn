from turtle import *

speed(0)
bgcolor('teal')
color('yellow') 
pensize(3)
for i in range(150):
    rt(i)
    circle(150, i)
    fd(i)
    rt(90)

hideturtle()
done() 