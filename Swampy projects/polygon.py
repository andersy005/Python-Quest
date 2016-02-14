from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def polygon(t, n, length):
    angle = 360.0/n
    for i in range(n):
        fd(t, length)
        rt(t, angle)

polygon(bob, n=7, length=100)

wait_for_user()