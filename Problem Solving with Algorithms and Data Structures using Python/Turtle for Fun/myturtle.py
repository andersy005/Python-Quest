import turtle

wn = turtle.Screen()
alexa = turtle.Turtle()

def drawSpiral(myTurtle, lineLen):
	if lineLen > 0:
		alexa.forward(lineLen)
		alexa.right(90)
		drawSpiral(alexa, lineLen-10)


drawSpiral(alexa,200)
wn.exitonclick()

