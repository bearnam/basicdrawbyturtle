import turtle
t = turtle.Pen()
t.shape('turtle')
t.color('green')
t.speed(300)
t.pencolor('purple')

def Rectangle():
    for i in range(4):
        t.fd(100)
        t.left(90)
        
def Go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def drawtraingle():
    for i in range(3):
        t.fd(100)
        t.left(120)

def drawtangle8():
    for i in range(20):
        t.fd(50)
        t.left(45)
        t.fd(100)
        t.left(95)


def drawflower1():
    for i in range(10):
        Go(0,0)
        drawtangle8()






