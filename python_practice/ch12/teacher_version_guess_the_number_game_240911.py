from random import randint

easy_level_turns = 10
hard_level_turns = 5

#실제 답을 추측하고 그 답이 정확한지 체크하는 기능 구현
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("too high.")
    elif user_guess <  actual_answer:
        print("too low")
    else:
        print(f"you got it ! the answer was {actual_answer}")
# 1~10까지 랜덤 점수 선택




print("welcome to the number guessing game!")
print("i'm thinking of a number between 1 ~ 100")
answer = randint(a=1, b=100)
print(f"pssst, the correct answer is {answer}")

# 난이도 기능 설정
def set_difficulty():
    while True:
        level = input("choose a difficulty. type 'easy' or 'hard'")
        if level == 'easy':
            return easy_level_turns # break는 반환값 없이 종료 , return 은 반환값 출력하며 종료 
        elif level == 'hard':
            return hard_level_turns
        else :
            print("choose the 'easy' or 'hard'")




# 숫자 추측
turns = set_difficulty() 
print(f"you have {turns}attempts remaining to guess the number")
guess = int(input("make a guess:"))


#만약 틀렸다면 기회를 1줄이는 기능 구현


#만약 그들이 틀렸다면 반복해서 추측하게 함

