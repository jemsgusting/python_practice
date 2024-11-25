'''
1. 뱀 몸통제작
2. 뱀 움직이기
3. 상하좌우 화살표로 뱀 움직이기
4. 뱀이 먹이를 먹으면 사이즈가 커지면서 다른 위치에 또 다른 음식이 생김
5. 먹이를 먹으면서 위에 점수가 올라가는걸 보여줌
6. 벽에 부딪히면 죽음 -> 게임 종료
7. 뱀이 본인 몸이나 꼬리에 부딪히면 -> 게임 종료 
'''
from turtle import *
from turtle import Screen, Turtle
import time 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("pink")
screen.title("My Snake Game")
screen.tracer(0) #애니메이션을 비활성화함

#첫번째 단계 - 뱀만들기
starting_positions = [(0,0),(-20,0),(-40,0)] #튜플 : 튜플을 제작해서 특정 값의 자료를 뽑아내서 사용하고 싶을때 사용하는 방법

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup() # 개체가 움직인 위치에 선이나 기록 등이 남지 않음
    new_segment.goto(position)
    segments.append(new_segment)


'''
뱀 움직이기
'''

game_is_on = True
while game_is_on:
    screen.update() # 수동으로 화면을 업데이트시키는 기능임, 원하는 시점에 화면 갱신시에 해당 함수를 사용하는 것 => 해당 메소드가 뱀이 끊어져서 움직이도록 보이게함 
    time.sleep(0.1) # 뱀의 몸통이 1초에 하나씩 움직임
    
    for seg_num in range(len(segments)-1, 0,-1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments.forward(20)
    
    
    for seg in segments:
        seg.forward(20)
        
        
screen.exitonclick() # 해당 행을 적어야 프로그램 실행시 창이 바로 사라지지 않음


'''
유데미 149번 강좌부터 수강하기
'''