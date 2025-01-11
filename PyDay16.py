'''
from turtle import *
timmy = Turtle()
timmy.color("red")
timmy.shape("circle")
for i in range(100):
    for j in ('yellow','blue','red','green'):
        color(j)
        forward(i)
        right(100)

my_screen = Screen()
print(my_screen.canvheight)  '''

from turtle import *
color('red')
fillcolor('yellow')

begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()