#블랙잭게임
#블랙잭 게임은 2개의 랜덤카드를 받은 후 두 카드의 합이 21에 가까운 사람이 이기는 게임이다.
#21을 넘으면 패배
#J K Q 은 각각 10으로 계산 , A(ace)는 총합에 1 혹은 11로 계산
#에이스의 경우 21을 넘었는지 넘지 않았는지에 따라 값이 1아니면 11로 결정된다.
#상대방의 카드의 합이 16이하인경우 반드시 카드를 한장 더 받아야함

import sys
import random

def play_the_game():
    replay_the_game = True
    while replay_the_game:
        print(
        '''
            __ _  __ __ __ ___   ___  ___ 
            / _` |/ _` | '_ ` _ \ / _ \/ __|
            | (_| | (_| | | | | | |  __/\__ |
            \__, |\__,_|_| |_| |_|\___||___/
            __/ |                          
            |___/                       

        ''')

        #카드 덱에 11이 있고 카드의 합, 즉 총 점수가 이미 21을 초과한 경우에 대한 조치

        add1 = 0  #값을 할당할때는 = 하나만 쓰고 비교연산자의 경우에만 == 2개를 사용한다 
        add2 = 0

        def calculate_score():
            if add1 >= 21 or add_two_ramdom_number >= 21:
                print("You went over. You lose")
                sys.exit()
            else: 
                pass

        random_number1 = random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,10,10])
        random_number2 = random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,10,10])
        add_two_ramdom_number = random_number1+random_number2
        print(f"your cards: [{random_number1},{random_number2}] , current score : {add_two_ramdom_number}")
        computer_first_card = random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,10,10])
        print(f"computer's first card: {computer_first_card}") # 상대방 카드는 하나는 까져있고 하나는 비공개다 
        calculate_score()


        def receive_new_card():
                print(f"your final hand : [{random_number1},{random_number2},{random_number3}], final score : {add1}")

        def no_receive_new_card():
                print(f"Your final hand : [{random_number1},{random_number2}] , final score : {add2}")

        select_type = input("Type 'y' to get another card, type 'n' to pass : n")
        if select_type == 'y': #카드를 추가로 받는 경우 
            random_number3 = random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,10,10])
            add1 = random_number1+random_number2+random_number3
            receive_new_card()
        else : # 추가로 받지 않는 경우 
            add2 = random_number1 + random_number2 
            no_receive_new_card()
        computer_second_card = random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,10,10])
        add_computer_cards = computer_first_card + computer_second_card
        print(f"computer's final hand : [{computer_first_card},{computer_second_card}] , final score: {add_computer_cards} ")
        calculate_score()
        
        print("final result!")
        if add1 > add_computer_cards:
            print("You are win!")
        elif add2 > add_computer_cards:
            print("You are win!")
        else :
            print("You went over. You lose")
        
        #아래는 한번더 게임을 플레이 할건지에 대한 여부 확인
        one_more_time_the_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'")
        if one_more_time_the_game == 'n':
            return 0
        elif one_more_time_the_game == 'y':
            print("\n" * 20)
            play_the_game()

#여기가 제일 처음 게임을 진행할건지에 대한 여부 확인
play_the_game_check = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if play_the_game_check == 'y':
    play_the_game()
else :
    sys.exit("프로그램을 종료합니다.")



#해당 첫 프로젝트 후기 24월 9월 9일 오후 10시 44분 
#입력이나 .append 등등 인수로 바아오고 이러한 부분은 활용이 아직 약하지만
#그래도 함수를 적재적소에 사용하여 제작하여 게임은 진행된다.

