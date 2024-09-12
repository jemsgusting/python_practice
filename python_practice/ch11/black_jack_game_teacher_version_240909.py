# 같은 블랙잭 게임인데 내가 만든것 말고 선생님이 만든 블랙잭 게임 예시
import random
def deal_card(): #덱에서 랜덤 카드 반환
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards) # 랜덤으로 하나만 선택하는 것것
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2: #len(cards) == 2는 cards 리스트에 요소가 2개인 경우 해당 if 문을 실행
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11) # 리스트에서 11을 제거 
        cards.append(1) # 11 대신 1을 추가하는 것 
    return sum(cards)

def compare(u_score, c_score): 
    #if, elif , else 에서 어떤 순서대로 처리해야하는지 의문이면 위에서 아래로 소스코드가 동작한다는 점을 인지하자 ! 
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose oppenent has blackjack" # opponent = 상대 
    elif u_score >= 21:
        return "you went over. you lose"
    elif c_score >= 21:
        return "Opponent went over. You win"
    elif u_score > c_score :
        return "You win! "
    else:
        return "You lose!"

def play_the_game():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1 
    is_game_over = False #사용자와 컴퓨터의 점수를 계속 계산하는 while 반복문 제작가능

    #여기서 카드를 분배해주는 과정이다
    for _ in range(2): #따로 특정 변수에 반복수행을 하는게 아니라면 변수이름 대신 _ 기입 가능 
        #user_card와 computer_cards의 빈리스트에 deal_card() 함수 호출로 입력시켜서 랜덤으로 카드를 user_card 리스트에 2번 넣는다. 
        user_cards.append(deal_card()) 
        computer_cards.append(deal_card())
        #append 기능을 사용하여 넣지 않고 += 를 통해 리스트에 넣는 경우 -> user_card += new_card 실행시 오류 발생함
        #append 함수는 user_card 리스트 뒤에 바로 확장시켜 deal_card()에서 반환되는 값을 연달아 리스트에 추가함

    while not is_game_over: # while is_game_over == False 도 가능 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards : {user_cards}, current score : {user_score}")
        print(f"computer's fist card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True #게임종료시 사용할 is_game_over 변수
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final score : {user_cards}, final score : {user_score}")
    print(f"computer's final hand : {computer_cards}, final score : {computer_score}")
    print(compare(user_score, computer_score)) # 결과 출력 

while input("Do you want to play a game of blackjack? Type 'y' or 'n' = ") == 'y':
    print("\n"*20)
    play_the_game()
