from turtle import Turtle, Screen
import random
from math import cos, radians

# swarmSize = 25
# t = turtle.Turtle()
# win = turtle.Screen()
# win.setworldcoordinates(-600,-600,600,600)
# t.speed(10)
# t.tracer(15)

# swarm = []

# def getNewHeading(i):
	
# 	'''The expression cos(radians(head)) determines whether the other object swarm[j] is in front of or behind the object swarm[i]. 
# 	We define in front of to be based on the heading of the object swarm[i]. This is important because we are assuming that you 
# 	can only see objects in front of you.'''



# 	minangle = 999
# 	for j in range(swarmSize):
# 		if i != j:
# 			head = swarm[i].towards(swarm[j]) - swarm[i].heading()
# 			infront = cos(radians(head))

# 			if infront > 0:
# 				if head < minangle:
# 					minangle = head
# 	return minangle

# for i in range(swarmSize):
# 	nt =  turtle.Turtle()
# 	swarm.append(nt)
# 	nt.up()
# 	nt.setheading(random.randrange(360))
# 	nt.setpos(random.randrange(-300,360), random.randrange(-300,300))
# 	nt.down()

# for turn in range(100):
# 	'''Once all of the decisions are made then we can go back and implement the decisions and update our display of the world swarm[i].
# 	setheading(newhead[i]) This is a good example of parallel array construction. Where the new heading for swarm[i] is in newhead[i].
# '''
# 	newhead = []
# 	for i in range(swarmSize):
# 		minangle = getNewHeading(i)
# 		if minangle == 999:
# 			newhead.append(swarm[i].heading())
# 		else:
# 			newhead.append(minangle + swarm[i].heading())

# 	for i in range(swarmSize):
# 		swarm[i].setheading(newhead[i])
# 		swarm[i].forward(10)


# win.exitonclick()

# object oriented implementation

class Schooler(Turtle):
	swarm = []

	def __init__(self):
		Turtle.__init__(self)
		self.up()
		self.setheading(random.randrange(360))
		self.setpos(random.randrange(-200,200), random.randrange(-200,200))
		self.down()
		self.newhead = None
		Schooler.swarm.append(self)


	def getNewHeading(self):
		minangle = 999
		for other in Schooler.swarm:
			if self != other:
				head = self.towards(other) - self.heading()
				if cos(radians(head)) > 0 :
					if head < minangle:
						minangle = head

		if minangle == 999:
			self.newhead = self.heading()

		else:
			self.newhead = minangle + self.heading()

	def setHeadingAndMove(self):
		self.setheading(self.newhead)
		self.newhead = None
		self.forward(10)


def main():
	swarmSize = 25
	t = Turtle()
	win = Screen()
	win.setworldcoordinates(-600,-600,600,600)
	t.speed(10)
	t.tracer(15)
	t.hideturtle()

	for i in range(swarmSize):
		Schooler()

	for turn in range(50):
		for schooler in Schooler.swarm:
			schooler.getNewHeading()

		for schooler in Schooler.swarm:
			schooler.setHeadingAndMove()

	win.exitonclick()

main()
