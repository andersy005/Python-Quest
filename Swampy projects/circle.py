from swampy.TurtleWorld import *
from math import *

world = TurtleWorld()
bob = Turtle()


def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        rt(t, angle)


# def circle(t, radius):
#   circumference = 2 * pi * radius   # Circumference of the circle
#   n = 50                            # n is the number of line segments in our approximation of a circle: 50 sided

#    length = circumference / n
#   polygon(t, n, length)


def circle(t, r):
    circumference = 2 * pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)


circle(bob, 250)

wait_for_user()
