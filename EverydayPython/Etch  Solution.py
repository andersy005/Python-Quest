import turtle

class Etch(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.myWn = turtle.Screen()
		self.color('blue')
		self.speed(0)
		self.dist = 5
		self.myWn.onkey(self.up,"l")
		self.myWn.onkey(self.down, "j")
		self.myWn.onkey(self.left,"a")
		self.myWn.onkey(self.right,"d")
		self.myWn.onkey(self.quit,"q")
		self.myWn.listen()


	def up(self):
		self.goto(self.xcor(), self.ycor() + self.dist)

	def up(self):
		self.goto(self.xcor(), self.ycor() - self.dist)

	def up(self):
		self.goto(self.xcor() - self.dist, self.ycor())

	def up(self):
		self.goto(self.xcor() + self.dist,  self.ycor())

	def quit(self):
		self.myWn.bye()

	def main(self):
		turtle.mainloop()

if __name__  == '__main__':
	etch = Etch()
	etch.main()

