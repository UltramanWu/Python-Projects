from turtle import *

setup(650,350)
penup()
fd(-300)
pendown()
pensize(25)
pencolor('red')
seth(-40)
for i in range(4):
    circle(40,80)
    circle(-40,80)
circle(40,80/2)
fd(40)
circle(30,180)
fd(50)
done()


