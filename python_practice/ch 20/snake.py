from turtle import *

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("yellow")
        new_segment.penup()
        new_segment.goto(position) 
        self.segments.append(new_segment)

    def extend(self): # 뱀의 몸길이 증가
        self.add_segment(self.segments[-1].position())  # [=1]은 예를 들어 인덱스에 [1,2,3]이 존재하면 거꾸로인 3부터 세는 것이다.


    def move(self):
        #거북이 위치 이동
        for seg_num in range(len(self.segments) -1 ,0 ,-1): # start=2 , stop=0 , step=-1
            new_x = self.segments[seg_num - 1].xcor() # 이전 거북이의 X좌표 # xcor은 그 객체가 위치한 x 좌표값을 반환하는 것 
            new_y = self.segments[seg_num - 1].ycor() # 이전 거북이의 Y좌표
            self.segments[seg_num].goto(new_x,new_y) #이전 거북이의 x,y 좌표로 하나씩 이동을 시키는것 
        self.segments[0].forward(MOVE_DISTANCE) # ㅇ ㅇ ㅇ 이렇게 있었으면 왼쪽에서 두번째까지 애들은 이전 거북이의 x,y 좌표로 하나씩 이동 시키는데 제일 오른쪽 ㅇ 애는 새로운 경로로 하나씩 움직여줘야하니까 앞으로 20픽셀씩 움직이게한것 
    
# 수학의 1,2,3,4 분면을 기준으로 했을때 각 각도들이 해당 위치들을 의미함

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        # 위쪽으로 이동하는 동작을 정의

    def down(self):
        # 아래쪽으로 이동하는 동작을 정의
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        # 왼쪽으로 이동하는 동작을 정의
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        # 오른쪽으로 이동하는 동작을 정의
        if self.head.heading() != 180:
            self.head.setheading(0)
