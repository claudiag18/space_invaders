import turtle
from player import Player
from invader import Invader
from barrier import Block
from score import Score
import time

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("SPACE INVADERS")
screen.bgpic("background.gif")
screen.listen()
screen.tracer(0)

# REGISTERING NEW SHAPES
turtle.register_shape("invader2.gif")
turtle.register_shape("invaderA2.gif")
turtle.register_shape("invaderB2.gif")
turtle.register_shape("invaderC2.gif")
turtle.register_shape("player2.gif")


# CREATING PLAYER
player = Player()
player.initial_position((0, -220))
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")
screen.onkey(player.shoot, "space")

# CREATING ROW OF INVADERS
invaders = Invader()
invaders.invader_formation()


# CREATING BARRIERS
blocks = Block()
blocks.block_formation()


# CREATING SCORE BOARD
score = Score()

game_on = True

while game_on:
    time.sleep(invaders.move_speed)
    screen.update()
    player.bullet_move()
    invaders.invader_move()
    invaders.invader_droplet()
    invaders.droplet_move()
    # Detecting collision bullet - invader:
    for invader in invaders.invaders:
        for bullet in player.bullets:
            if bullet.distance(invader) < 20:
                invader.goto((2000, 2000))
                bullet.goto((3000, 3000))
                score.increase_points()
    # Detecting collision bullet - barrier:
    for block in blocks.blocks:
        for bullet in player.bullets:
            if bullet.distance(block) < 5:
                block.goto((4000, 4000))
                bullet.goto((3000, 3000))
    # Detecting collision droplet - barrier:
    for block in blocks.blocks:
        for droplet in invaders.droplets:
            if droplet.distance(block) < 10:
                block.goto((4000, 4000))
                droplet.goto((2000, 2000))
    # Detecting collision droplet - player:
    for droplet in invaders.droplets:
        if droplet.distance(player) < 25 and score.score > 0:
            droplet.goto((2000, 2000))
            player.initial_position((0, -220))
            score.decrease_score()
        if droplet.distance(player) < 25 and score.score == 0:
            droplet.goto((2000, 2000))
            player.goto((1000, 1000))
            score.game_over()
    # Detecting collision droplet - bullet:
    for bullet in player.bullets:
        for droplet in invaders.droplets:
            if droplet.distance(bullet) < 10:
                bullet.goto((3000, 3000))
                droplet.goto((2000, 2000))
    # Detecting if any invader left:
    i = 0
    for invader in invaders.invaders:
        if invader.xcor() > 800:
            i += 1
        if i == 32:
            score.win_game()
    if invaders.counter == 10:
        score.game_over()
        player.goto((1000, 1000))
        invaders.move_speed = 0




screen.exitonclick()