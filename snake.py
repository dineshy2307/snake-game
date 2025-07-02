from turtle import Turtle

class Snake:

    def __init__(self):
        self.length = 3
        self.turtles = []
        t = -20
        for i in range(self.length):
            self.turtles.append(Turtle("square"))
            self.turtles[i].penup()
            self.turtles[i].color("white")
            self.turtles[i].setx(t * i)
            self.turtles[i].speed(2)

    def move(self):
        for i in range(self.length-1, 0, -1):
            self.turtles[i].setpos(self.turtles[i-1].xcor(), self.turtles[i-1].ycor())
            self.turtles[i].setheading(self.turtles[i-1].heading())
        self.turtles[0].forward(20)
        return self.check()

    def grow(self):
        self.turtles.append(Turtle("square"))
        self.turtles[-1].penup()
        self.turtles[-1].color("white")
        self.turtles[-1].setpos(self.turtles[-2].xcor(), self.turtles[-2].ycor())
        self.turtles[-1].setheading(self.turtles[-2].heading())
        self.turtles[-1].speed(2)
        self.length += 1

    def up(self):
        if self.turtles[0].heading() == 0 or self.turtles[0].heading() == 180:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() == 0 or self.turtles[0].heading() == 180:
            self.turtles[0].setheading(270)

    def right(self):
        if self.turtles[0].heading() == 270 or self.turtles[0].heading() == 90:
            self.turtles[0].setheading(0)

    def left(self):
        if self.turtles[0].heading() == 270 or self.turtles[0].heading() == 90:
            self.turtles[0].setheading(180)

    def check(self):
        if self.turtles[0].xcor()>=300 or self.turtles[0].xcor()<=-300 or self.turtles[0].ycor()>=300 or self.turtles[0].ycor()<=-300 :
            return False
        else :
            return True