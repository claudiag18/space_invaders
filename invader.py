from turtle import Turtle
import random

INVADERS_SHAPE = ['invader2.gif', 'invaderA2.gif', 'invaderB2.gif', 'invaderC2.gif']


class Invader(Turtle):

    def __init__(self):
        super(). __init__()
        self.invaders = []
        self.move_speed = 0.15
        self.next_x = 10
        self.next_y = 0
        self.ghost_r = Turtle()
        self.ghost_l = Turtle()
        self.droplets = []
        self.counter = 0

    def invader_formation(self):
        self.ghost_r.shape('square')
        self.ghost_r.shapesize(stretch_wid=2.25, stretch_len=1.5)
        self.ghost_r.penup()
        self.ghost_r.speed(self.move_speed)
        self.ghost_r.goto(x=350, y=400)
        self.ghost_l.shape('square')
        self.ghost_l.shapesize(stretch_wid=2.25, stretch_len=1.5)
        self.ghost_l.penup()
        self.ghost_l.speed(self.move_speed)
        self.ghost_l.goto(x=0, y=400)
        for i in range(4):
            for j in range(8):
                new_invader = Turtle()
                new_invader.shape(INVADERS_SHAPE[i])
                new_invader.shapesize(stretch_wid=1, stretch_len=1)
                new_invader.penup()
                new_invader.speed(self.move_speed)
                new_invader.goto(x=0 + (j*50), y=260 - (i*30))
                self.invaders.append(new_invader)


    def invader_move(self):
        drop_level = False
        ghost_r_x = self.ghost_r.xcor()
        ghost_l_x = self.ghost_l.xcor()
        if ghost_r_x >= 350 or ghost_l_x <= -350:
            self.next_x *= -1
            drop_level = True
            self.counter += 1
            self.move_speed *= 0.5
        if drop_level:
            self.next_y = -30
            f = 0
        else:
            self.next_y = 0
            f = 1
        for invader in self.invaders:
            current_x = invader.xcor()
            current_y = invader.ycor()
            invader.goto(x=current_x + f*self.next_x, y=current_y + self.next_y)
        self.ghost_r.goto(x=ghost_r_x + self.next_x, y=400)
        self.ghost_l.goto(x=ghost_l_x + self.next_x, y=400)


    def invader_droplet(self):
        num = random.randint(1, 6)
        if num == 3:
            i = 0
            for invader in self.invaders:
                if invader.xcor() < 800:
                    i += 1
            if i > 0:
                ind = random.randint(0, i-1)
                droplet = Turtle()
                droplet.shape("circle")
                droplet.color('white')
                droplet.shapesize(stretch_wid=0.3, stretch_len=0.2)
                droplet.penup()
                droplet.goto(self.invaders[ind].xcor(), self.invaders[ind].ycor())
                droplet.speed(0.05)
                self.droplets.append(droplet)

    def droplet_move(self):
        for droplet in self.droplets:
            droplet_x = droplet.xcor()
            current_droplet_y = droplet.ycor()
            droplet.goto(x=droplet_x, y=current_droplet_y - 10)
