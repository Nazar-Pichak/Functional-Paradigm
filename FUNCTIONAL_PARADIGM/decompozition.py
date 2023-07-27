import turtle

def move(a):
    turtle.forward(a)
    turtle.left(90)

def square(a):
    for i in range(4):
        move(a)

def squareColor(a, color):
    turtle.color(color)
    turtle.begin_fill()
    square(a)
    turtle.end_fill()

turtle.speed(1)

squareColor(50, 'red')

turtle.goto(100, 100)
squareColor(80, 'green')

