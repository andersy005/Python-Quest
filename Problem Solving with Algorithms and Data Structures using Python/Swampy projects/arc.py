from swampy.TurtleWorld import *
from math import*

world = TurtleWorld()
bob = Turtle()

def arc(t, r, angle):
    arc_length =  2 * pi * r * angle/360
    n = int ( arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle)/ n

    for i in range(n):
        fd(t, step_length)
        rt(t, step_angle)

    rt(t)
    fd(t,r)


arc(bob, 200, 90)
wait_for_user()