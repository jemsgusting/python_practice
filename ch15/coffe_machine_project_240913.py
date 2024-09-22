#만들맛 - 에스프레소 , 라떼 , 카푸치노
'''
3가지 음료 레시피


미국동전 4가지 종류 존재
달러도 예전에 동전이 있었음 
동전의 가치가 뭔지 주목
페니 1
니켈 5
다임 10 센트
쿼터 1달러의 4분의 1 = 0.25

프로그램 요구사항 분석
커피머신은 보고서를 출력해야한다. 남은 자원뭔지 남은물의 양이나 우유의 남은양

# 1. print report => print 입력
물, 우유, 커피 의 필요량과 금액
커피종류를 선택시 => 커피 입력하라고 먼저 말하고 
쿼터, 다임, 니클, 페니스 요금별 지불해야하는 금액 기입
지불 후 잔돈반환
라떼 여기있습니다 ! 즐기세요 ! 멘트 날리기

# 2. check resources sufficient?
물이 부족한지 우유가 부족한지 사용자한테 알려주기 
자원중 부족한게있으면 음ㄹ료만들수 없고 피드백 제공
-> 자원이 충분한가 ? 

# 3. Process coins
#돈부족하면 돈 부족하다고 돈 반환해주기 -> Sorry that's not enough money. Money refunded
-> 그리고 다시 재묻기 -> what would you like ? 

# 4. check transaction successful? 
#만약 충분히 돈을 넣었다면
이 모든 동전의 실제 금액을 계산하고 음료 비용을 Here is $000 in change. 보여줌
Here is your [선택한것 ] Enjoy! 출력하기


#라떼 만들기 전에 우유 300ml 있었습니다 . 
근데 라떼 만든 후에 보고서 요청하면
물이 줄고 우유 줄어들고 커피가 줄어들고 대신 돈이 금고에 들어간걸 볼수 있음



'''
#TODO : 2.음료주문 만들기에 자원이 충분한지 확인

machine_on = True
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}
global add_num 
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_coffee(what_coffee, order_ingredients):
    #필요한 재료를 자원에서 차감
    for item in order_ingredients:
        resources[item] -= order_ingredients[item] 
    print(f"here is your {what_coffee}. enjoy ! ")



def coin(): #5번 항목 - 동전을 처리합니다
    print("quarter: $0.25, dime: $0.10, nickel: $0.05, penny : $0.01")
    num = [int(input("put in the coin count")) for _ in range(4)] #코인 별 값을 순서대로 입력받음
    print(f"quater : {num[0]}, dime : {num[1]}, neckel : {num[2]}, penny : {num[3]}")
    global add_num 
    add_num = (0.25*num[0]) + (0.10*num[1]) + (0.05*num[2]) + (0.01*num[3])
    return add_num
    
def is_transaction_successful(money_received, drink_cost):
    #돈지불이 제대로 됐는지 안됐는지 확인
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2) #round는 계산된 값을 소수점 n자리까지 반올림 하는 함수인데 뒤에 2를 기입했으니 2자리까지 반올림 하는 함수이다. 
        print(f"here is ${change} in change.") #잔돈 반환값 돌려준다고 알림
        global add_num
        add_num += drink_cost #report에서 보여질 값을 위해 값을 더해서 저장시킴
        return True
    else:
        print("sorry that's not enough money.Money refunded")
        return False

def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"{item}이 충분하지 않습니다")
            is_enough  = False
    return is_enough


while machine_on: #커피 머신 필수 동작
    print("\n" * 10) 
    print("select espresso/latte/cappuccino")
    print("report : remain resource & show price")
    print("if you want to end the machine, you input the 'off'")
    what_coffee = input("what do you like? ")
    if what_coffee == 'report':#현재자원값
        print(f"water : {resources['water']}")
        print(f"Milk : {resources['milk']}")
        print(f"Coffee : {resources['coffee']}")
        print(f"Money : ${add_num}")
    elif what_coffee == 'off':
        machine_on = False
    else:
        drink = MENU[what_coffee]
        if is_resource_sufficient(drink["ingredients"]):
            payment = coin() # coin반환값이 payment에 저장됨
            #payment 는 거래가 성공했는지 확인하는 다음단계로 넘어감 
            #음료 실제구매가능한만큼 충분한 돈 투입했는지 확인해야함
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(what_coffee, drink["ingredients"])
