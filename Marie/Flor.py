import turtle
import random
from turtle import *
from math import *

header_text= " Solo para recordarte que: "
color("Blue")
penup()
goto(-325,600)
pendown()
write(header_text, align="left", font=("Arial", 12, "normal"))
header_text= " !!!Esto es una simulacion!!!"
color("Purple")
penup()
goto(-325,500)
pendown()
write(header_text, align="left", font=("Arial", 12, "normal"))
header_text= " Despierta Marie[°•°]"
color("red")
penup()
goto(-325,-550)
pendown()
write(header_text, align="left", font=("Arial", 12, "normal"))

speed(0)
bgcolor("white")
goto(0, -40)

for i in range(16):
    for j in range(18):
        color('#000000'), rt(90)
        circle(150-j*6, 90), lt(90)
        circle(150-j*6, 90), rt(180)
    circle(40, 24)

color('black') 
shape('circle')
shapesize(0.5)
fillcolor('#55158D')
golden_ang = 137.508
phi = golden_ang * (pi / 180)

for i in range(140):
    r = 4 * sqrt(i)
    theta = i * phi
    penup(), goto(x=r*cos(theta), y=r*sin(theta))
    setheading(i * golden_ang)
    pendown(), stamp()

def draw_all_seeing_eye(x, y):
    penup()
    goto(x, y)
    pendown()
    color('white')
    begin_fill()
    circle(25)  
    end_fill()

    # Draw the pupil
    penup()
    goto(x, y)
    pendown()
    color('red')
    begin_fill()
    circle(10)  # Pupil
    end_fill()

draw_all_seeing_eye(20, -30)  


screen = turtle.Screen()
screen.setup(width=1000, height=1000)  
screen.bgcolor("white")  

mandala = turtle.Turtle()
mandala.speed(0) 
mandala.hideturtle()

dark_colors = ["#111111", "#222222", "#333333", "#444444", "#555555", "#666666"]

def draw_concentric_circles(radius, layers):
    for _ in range(layers):
        mandala.penup()
        mandala.goto(0, -radius)
        mandala.pendown()
        mandala.color(random.choice(dark_colors))
        mandala.circle(radius)
        radius += 25

def draw_rotating_squares(size, layers, angle):
    for _ in range(layers):
        mandala.penup()
        mandala.goto(0, 0)
        mandala.pendown()
        mandala.color(random.choice(dark_colors))
        for _ in range(4):
            mandala.forward(size)
            mandala.right(90)
        mandala.right(angle)
        size += 30  
def draw_expanding_mandala():
    draw_concentric_circles(50, 30)  
    
    draw_rotating_squares(50, 40, 10)  

draw_expanding_mandala()

turtle.done()
