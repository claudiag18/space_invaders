from turtle import Turtle


class Block(Turtle):

    def __init__(self):
        super(). __init__()
        self.blocks = []


    def block_formation(self):
        for n in range(7):
            for i in range(4):
                for j in range(14):
                    new_block = Turtle()
                    new_block.shape('square')
                    new_block.color('white')
                    new_block.shapesize(stretch_wid=0.3, stretch_len=0.2)
                    new_block.penup()
                    new_block.goto(x=-350 + n*(105) + (j*5), y=-150 - (i*7))
                    self.blocks.append(new_block)