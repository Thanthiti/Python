import turtle as t 
import random

tim = t.Turtle()

def draw_shape():
    angle = 360 / 10

    for i in range(10):
        tim.forward(100)
        tim.right(80)
    pass

for sd in range(3,11):
    draw_shape()