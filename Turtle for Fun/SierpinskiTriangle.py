import turtle

def drawTriangle(points,color,siri):
	siri.fillcolor(color)
	siri.up()
	siri.goto(points[0][0], points[0][1])
	siri.down()
	siri.begin_fill()
	siri.goto(points[1][0], points[1][1])
	siri.goto(points[2][0], points[2][1])
	siri.goto(points[0][0], points[0][1])
	siri.end_fill()


def getMid(p1, p2):
	return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)


def main():
	siri = turtle.Turtle()
	myWin = turtle.Screen()
	mypoints =[[-100,-50], [0,100],[100,-50]]
	sierpinski(mypoints,3,siri)
	myWin.exitonclick()

main()