from turtle import *

speed('fastest')

def polygon(sides, length, color, width):
    pencolor(color)
    pensize(width)
    for i in range(sides):
        forward(length)
        right(360/sides)
#calling
polygon(4, 100, 'red', 5)

hideturtle()
mainloop()