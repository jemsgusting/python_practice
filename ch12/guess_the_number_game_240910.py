<<<<<<< HEAD
#Guess the number game 
import random

attempt = 10

def create_random_number_choice():
    random_num_list = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    return random.choice(random_num_list)
    

def easy_version():
    random_number = create_random_number_choice()
    for repeat in range(attempt,0,-1): #attempt = 10에서 0이될까지 -1씩 반복하는 것 
        answer = int(input("Make a guess : "))
        if answer < random_number :
            print(f"you have {repeat} attempts remaining to guess the number.")
            print("too low.")
            print("number is higher than your guess")
        elif answer > random_number :
            print(f"you have {repeat} attempts remaining to guess the number.")
            print("too high.")
            print("number is lower than your guess")
        elif answer == random_number :
            print("correct !")
            break # 이게 맞추면 for문을 나가는 역할 
    else:
        print("you lose")
    print(f"The answer was {random_number}.")
        
def play_game():
    print("welcome to the Number Guessing Game!")
    print("I thinking of a Number between 1 and 100.")
    choose_type = input("choose a difficulty. Type 'easy' or 'hard':")
    if choose_type == 'easy':
        easy_version()

while True:
    play_game()
    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again == 'no':
        break
    elif play_again == 'yes':
        play_game()

# 내가 게임을 챗gpt를 통해서 만들었고
# 강의에서 선생님이 만드는 부분 확인하고 선생님 버전도 만들어보기 








    
    
=======
#Guess the number game 
import random

attempt = 10

def create_random_number_choice():
    random_num_list = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    return random.choice(random_num_list)
    

def easy_version():
    random_number = create_random_number_choice()
    for repeat in range(attempt,0,-1): #attempt = 10에서 0이될까지 -1씩 반복하는 것 
        answer = int(input("Make a guess : "))
        if answer < random_number :
            print(f"you have {repeat} attempts remaining to guess the number.")
            print("too low.")
            print("number is higher than your guess")
        elif answer > random_number :
            print(f"you have {repeat} attempts remaining to guess the number.")
            print("too high.")
            print("number is lower than your guess")
        elif answer == random_number :
            print("correct !")
            break # 이게 맞추면 for문을 나가는 역할 
    else:
        print("you lose")
    print(f"The answer was {random_number}.")
        
def play_game():
    print("welcome to the Number Guessing Game!")
    print("I thinking of a Number between 1 and 100.")
    choose_type = input("choose a difficulty. Type 'easy' or 'hard':")
    if choose_type == 'easy':
        easy_version()

while True:
    play_game()
    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again == 'no':
        break
    elif play_again == 'yes':
        play_game()

# 내가 게임을 챗gpt를 통해서 만들었고
# 강의에서 선생님이 만드는 부분 확인하고 선생님 버전도 만들어보기 








    
    
>>>>>>> 5869b6b (	new file:   python_practice/ch10/calculator_240908.py)
