from turtle import *
from random import randint

speed(5)
goto(-140, 140)

penup()
for paso in range(14):
    write(paso, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup() 
    backward(160)
    left(90)
    forward(20)

ana = Turtle()
ana.color('red')
ana.shape('turtle')

ana.penup()
ana.goto(-160, 40)
ana.pendown()

juan = Turtle()
juan.color('green')
juan.shape('turtle')

juan.penup()
juan.goto(-160, 20)
juan.pendown()

alex = Turtle()
alex.color('yellow')
alex.shape('turtle')

alex.penup()
alex.goto(-160, 60)
alex.pendown()

isa = Turtle()
isa.color('pink')
isa.shape('turtle')

isa.penup()
isa.goto(-160, 80)
isa.pendown()

edu = Turtle()
edu.color('blue')
edu.shape('turtle')

edu.penup()
edu.goto(-160, 100)
edu.pendown()

for turn in range(100):
    ana.forward(randint(1, 5))
    juan.forward(randint(1, 5))
    alex.forward(randint(1, 5))
    isa.forward(randint(1, 5))
    edu.forward(randint(1, 5))

for giro in range(8):
    ana.right(randint(1, 5))
    juan.right(randint(1, 5))
    alex.right(randint(1, 5))
    isa.right(randint(1, 5))
    edu.right(randint(1, 5))