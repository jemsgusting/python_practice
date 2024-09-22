<<<<<<< HEAD
enemies = 1


def increase_enemies():
    enemies = 2     #이 enemies는 지역범위 내에서만(함수안에서만)적용됨 
    print(f"enemies inside function: {enemies}") #2

increase_enemies()
print(f"enemies outside function: {enemies}") #얘는 전역변수인 enemies의 값을 가져와서 1을 출력


'''
지역범위 = 함수내에 존재
전역범위 = 함수 외부에 존재해서 모든 변수에 할당 가능한 범위

위 코드의 예에서 enemies가 전역변수고 함수내에 있는 enemies가 지역변수이다.
=======
enemies = 1


def increase_enemies():
    enemies = 2     #이 enemies는 지역범위 내에서만(함수안에서만)적용됨 
    print(f"enemies inside function: {enemies}") #2

increase_enemies()
print(f"enemies outside function: {enemies}") #얘는 전역변수인 enemies의 값을 가져와서 1을 출력


'''
지역범위 = 함수내에 존재
전역범위 = 함수 외부에 존재해서 모든 변수에 할당 가능한 범위

위 코드의 예에서 enemies가 전역변수고 함수내에 있는 enemies가 지역변수이다.
>>>>>>> 5869b6b (	new file:   python_practice/ch10/calculator_240908.py)
'''