<<<<<<< HEAD
#행맨게임 ㅈㄴ 어렵네 ㅅㅂ
word_list = ["jemin", "banana", "thisgameissohard"]

import random


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f'Pssst, the solution is {chosen_word}')

display = [] #리스트 생성
for _ in range(len(chosen_word)): #단어 길이만큼 리스트내에 _ 생성
    display += "_"

end_of_game = False 
have_a_chance = 0
lives = 6
guess = ''

while not end_of_game: #게임이 끝날때까지 빈칸에 뭘 넣을건지에 대한 질문 반복시키기

    if guess in display:
        print(f"you've already guessed {guess}")

    guess = input("Guess a letter: ").lower() #질문
    for position in range(len(chosen_word)): #콘솔창에 보여질 position 변수에 접근할 수 있도록함
        letter = chosen_word[position] #랜덤으로 선택된 단어를 letter 이라는 곳에 저장함
        if letter == guess: #입력한 추측값이랑 letter 랑 동일한지 확인 여부
            display[position] = letter #display 라는 콘솔창에 보여질 리스트안에 해당 단어 집어넣음

        if guess not in chosen_word:
            print(f"you guessed {guess}, that's not in the word. you lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game=True
                print("u lose")

        print(f"{' '.join(display)}")
    
        if have_a_chance in range(1,6):
                
                if have_a_chance(1):
                    print('''    _______
                                    |/      |
                                    |      
                                    |      
                                    |       
                                    |      
                                    |
                                jgs_|___''') 
                elif have_a_chance(2):
                    print('''    _______
                                    |/      |
                                    |      (_)
                                    |      
                                    |       
                                    |      
                                    |
                                jgs_|___''') 
                elif have_a_chance(3):
                    print('''    _______
                                    |/      |
                                    |      (_)
                                    |       |
                                    |       |
                                    |      
                                    |
                                jgs_|___''') 
                elif have_a_chance(4):
                    print('''    _______
                                    |/      |
                                    |      (_)
                                    |      \|/
                                    |       |
                                    |      
                                    |
                                jgs_|___''') 
                elif have_a_chance(5):
                    print('''    _______
                                    |/      |
                                    |      (_)
                                    |      \|/
                                    |       |
                                    |      / \
                                    |
                                jgs_|___''') 
                elif have_a_chance(6):
                    print("it's done")
                    
        
        print(display)


    if "_"not in display:
        end_of_game = True
        print("you win!")



print(stages[lives])

'''
졌을때 와일문 나가는것
질때도 게임종료되는 조건 추가
stages 변수를 유저에게 남은 목숨에 알맞게 출력하는게 목적
플레이하며 글자 틀릴때마다 행맨이 ㄱ때그때 그려짐
결구 전체가 그려져서 게임이 끝나고 우리가 졌다고 나와야함
=======
#행맨게임 ㅈㄴ 어렵네 ㅅㅂ
word_list = ["jemin", "banana", "thisgameissohard"]

import random


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f'Pssst, the solution is {chosen_word}')

display = [] #리스트 생성
for _ in range(len(chosen_word)): #단어 길이만큼 리스트내에 _ 생성
    display += "_"

end_of_game = False 
have_a_chance = 0
lives = 6
guess = ''

while not end_of_game: #게임이 끝날때까지 빈칸에 뭘 넣을건지에 대한 질문 반복시키기

    if guess in display:
        print(f"you've already guessed {guess}")

    guess = input("Guess a letter: ").lower() #질문
    for position in range(len(chosen_word)): #콘솔창에 보여질 position 변수에 접근할 수 있도록함
        letter = chosen_word[position] #랜덤으로 선택된 단어를 letter 이라는 곳에 저장함
        if letter == guess: #입력한 추측값이랑 letter 랑 동일한지 확인 여부
            display[position] = letter #display 라는 콘솔창에 보여질 리스트안에 해당 단어 집어넣음

        if guess not in chosen_word:
            print(f"you guessed {guess}, that's not in the word. you lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game=True
                print("u lose")

        print(f"{' '.join(display)}")
    
        if have_a_chance in range(1,6):
                
                if have_a_chance(1):
                    print('''    _______
                                    |/      |
                                    |      
                                    |      
                                    |       
                                    |      
                                    |
                                jgs_|___''') 
                elif have_a_chance(2):
                    print('''    _______
                                    |/      |
                                    |      (_)
                                    |      
                                    |       
                                    |      
                                    |
                                jgs_|___''') 
                elif have_a_chance(3):
                    print('''    _______
                                    |/      |
                                    |      (_)
                                    |       |
                                    |       |
                                    |      
                                    |
                                jgs_|___''') 
                elif have_a_chance(4):
                    print('''    _______
                                    |/      |
                                    |      (_)
                                    |      \|/
                                    |       |
                                    |      
                                    |
                                jgs_|___''') 
                elif have_a_chance(5):
                    print('''    _______
                                    |/      |
                                    |      (_)
                                    |      \|/
                                    |       |
                                    |      / \
                                    |
                                jgs_|___''') 
                elif have_a_chance(6):
                    print("it's done")
                    
        
        print(display)


    if "_"not in display:
        end_of_game = True
        print("you win!")



print(stages[lives])

'''
졌을때 와일문 나가는것
질때도 게임종료되는 조건 추가
stages 변수를 유저에게 남은 목숨에 알맞게 출력하는게 목적
플레이하며 글자 틀릴때마다 행맨이 ㄱ때그때 그려짐
결구 전체가 그려져서 게임이 끝나고 우리가 졌다고 나와야함
>>>>>>> 5869b6b (	new file:   python_practice/ch10/calculator_240908.py)
'''