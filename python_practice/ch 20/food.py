from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self): # 먹이 먹으면 먹이 위치 바뀜
        random_x = random.randint(-200, 280)
        random_y = random.randint(-200, 280)
        self.goto(random_x, random_y)