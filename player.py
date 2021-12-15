from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super(). __init__()
        self.shape("player2.gif")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.bullets = []

    def initial_position(self, position):
        self.goto(position)

    def move_right(self):
        current_y = self.ycor()
        current_x = self.xcor()
        self.goto(x=current_x + 20, y=current_y)

    def move_left(self):
        current_y = self.ycor()
        current_x = self.xcor()
        self.goto(x=current_x - 20, y=current_y)

    def shoot(self):
        bullet = Turtle()
        bullet.shape("square")
        bullet.color('white')
        bullet.shapesize(stretch_wid=0.2, stretch_len=0.1)
        bullet.penup()
        bullet.goto(self.xcor(), -210)
        bullet.speed(0.05)
        self.bullets.append(bullet)



    def bullet_move(self):
        for bullet in self.bullets:
            bullet_x = bullet.xcor()
            current_bullet_y = bullet.ycor()
            bullet.goto(x=bullet_x, y=current_bullet_y + 5)
