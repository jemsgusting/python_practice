from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle) :

    def __init__(self):
        super().__init__()
        self.score = 0 # 점수판 점수 선언
        self.color("white") # 점수판 색깔
        self.penup() 
        self.goto(0,270) # y=270 위치에 점수판 배치
       # self.update_score()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT , font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)