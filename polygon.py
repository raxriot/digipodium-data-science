from turtle import *
def square():
    for i in range(4):
        fd (100)
        rt(90)
    
def pentagon():
    for i in range(5):
        fd(100)
        rt(72)
    
#calling
square()
pentagon()
goto(200,0)
square()
pentagon()

hideturtle()
mainloop()