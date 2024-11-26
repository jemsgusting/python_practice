#24/11/20~11/n

''' 개요
7개의 파일로 나눠서 만들어야함

1. 뱀 몸통 만들기
2. 뱀 움직이기
3. 뱀 먹이 만들기
4. 음식 감지 -> 새로운 먹이가 임의의 위치에 생겨야함
5. 점수보드 만들기
6. 벽으로부터 보호하기 
7. 꼬리로부터 보호하기 -> 몸이나 꼬리에 머리가 닿으면 죽음
'''

from turtle import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("pink") # 분홍 화면
screen.title("My snake game") # 제목
screen.tracer(0) # 화면에서 turtle 요소들이 끊기면서 움직이는것을 없애줌


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen() #입력된 키에 반응하는 명령어
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update() #screen.tracer과 같이 세트임 -> tracer로 화면에서 끊기는걸 없애고 update를 통해서 움직이고 난 후의 화면을 갱신해줌 
    time.sleep(0.1) #너무 빠른 요소의 시간을 1초 늦춤
    snake.move()
        
    '''
    #turtles에 있는 요소들을 하나씩 seg에 할당함
    그리고 turtles 리스트 요소들이 Turtle 객체라고 치면, seg는 순차적으로 그 Turtle 객체들을 가리킴  
    '''
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        print("nom nom nom")
        scoreboard.increase_score() # 음식 먹을때마다 점수증가 객체 선언

    # 벽에 부딪히면 죽는 것 
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # 꼬리로부터 보호하기
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:  # 10은 픽셀값을 의미하는데 두 객체가 사실상 겹쳐진 상태로 간주할만큼 겹쳐진 상태, 그래서 그것보다 작은 경우 죽음
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick() # 클릭하면 화면 종료 