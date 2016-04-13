from processing import *
from math import sin

X = 30
Y = 30
radius = 30

def setup():
	strokeWeight(10)
	frameRate(20)
	size(400,300)

def draw():
	global X, Y, radius
	delay = 16
	background(100)
	stroke(255)
	fill(0,121,184)

	X += (mouse.x-X)/delay;
	Y += (mouse.y-Y)/delay;

	radius = radius + sin(environment.frameCount / 4)

	ellipse(X,Y,radius,radius)