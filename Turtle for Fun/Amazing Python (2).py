import turtle
import random


def main():
    tList = []
    head = 0
    numTurtles = 10
    wn = turtle.Screen()
    wn.setup(500, 500)
    for i in range(numTurtles):
        nt = turtle.Turtle()  # make a new turtle, initialize values
        nt.setheading(head)
        nt.pensize(2)
        nt.color(random.randrange(255), random.randrange(255), random.randrange(255))
        nt.speed(10)
        wn.tracer(30, 0)
        tList.append(nt)  # Add the new turtle to the list
        head += 360 / numTurtles

    for i in range(100):
        moveTurtles(tList, 15, i)

    w = tList[0]
    w.up()
    #w.goto(0, 40)
    #w.write("Welcome ", True, "centC:\Python27er", "40pt Bold")
    #w.goto(0, -35)
    #w.write("World of Python ", True, "center", "20pt Bold")


def moveTurtles(turtleList, dist, angle):
    for turtle in turtleList:
        # Make every turtle on the list do the same actions
        turtle.forward(dist)
        turtle.right(angle)

main()
