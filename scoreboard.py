from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.speed(10)
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.setpos(0, 270)

    def up_score(self):
        self.score += 1

    def put_score(self):
        self.clear()
        self.write(f"Score : {self.score}", move=False, align="center", font=("Arial", 16, "bold"))

    def game_over(self):
        self.home()
        self.write(f"Game Over.", move=False, align="center", font=("Arial", 16, "bold"))