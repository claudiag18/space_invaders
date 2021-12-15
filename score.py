from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 3
        self.points = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(x=200, y=280)
        self.color("white")
        self.write(f"Score: {self.points}.  Plays left: {self.score}", move=False, align="center", font=("Verdana", 12, "normal"))
        self.hideturtle()


    def decrease_score(self):
        self.score -= 1
        self.score_update()


    def increase_points(self):
        self.points += 1
        self.score_update()


    def game_over(self):
        self.clear()
        self.penup()
        self.goto(x=0, y=0)
        self.color("white")
        self.write(f"GAME OVER.", move=False, align="center", font=("Verdana", 12, "normal"))
        self.hideturtle()


    def win_game(self):
        self.clear()
        self.penup()
        self.goto(x=0, y=0)
        self.color("white")
        self.write(f"YOU WIN!!!", move=False, align="center", font=("Verdana", 12, "normal"))
        self.hideturtle()