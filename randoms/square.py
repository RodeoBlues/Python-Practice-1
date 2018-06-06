import turtle

def sqr(draw_square):
	for i in range(0,4):
		draw_square.forward(100)
		draw_square.right(90)

def draws():
	window = turtle.Screen()
	window.bgcolor("red")

	john = turtle.Turtle()
	john.shape('turtle')
	john.speed(1)
	john.color('blue')
	sqr(john)

	mathew = turtle.Turtle()
	mathew.speed(1)
	mathew.circle(100)

	window.exitonclick()

draws()