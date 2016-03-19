from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

# print bob

def octagon(t, length, angle):
    for i in range(8):
        fd(t, length)
        rt(t, angle)

octagon(bob, 70, 45)

def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        rt(t,angle)


polygon(bob, 20, 100)
wait_for_user()