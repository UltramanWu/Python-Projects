# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/1 22:14
"""

import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main():
    turtle.setup(800, 800)
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.pendown()
    turtle.pensize(2)
    turtle.left(60)
    koch(400, 3)
    turtle.right(120)
    koch(400, 3)
    turtle.right(120)
    koch(400, 3)
    turtle.hideturtle()
    turtle.done()

main()