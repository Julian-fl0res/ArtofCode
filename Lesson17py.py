from random import *
from myfunctions import *
bob.speed(10)

screen = turtle.Screen()
screen.bgcolor("red")
screen.setup(width=800, height=600)

bob.width(5)


for number in range(100):
  bob.forward(number * 5)
  bob.left(91)
