from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def square(t, length):
    for i in range(4):
        fd(t, length)
        rt(t)

square(bob, 100)

wait_for_user()