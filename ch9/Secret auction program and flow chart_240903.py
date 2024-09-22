<<<<<<< HEAD
#비밀경매 프로그램과 순서도

'''
사람의 이름 = 키
입찰가 = Value

마지막에 모든 사람이 입찰 마칠시
그 딕셔너리 반복해서 누가 가장 높은 입찰했는지 알아내야함
'''

print("Welcom to the secret auction program.")
name = input("what is your name?:")
price = int(input("what's your bid?: $")) #명령하다, 분부를 내리다
should_continue = input("Are there any other bidders? Type 'yes' or 'no'")

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0 #최고 입찰가
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder 
    return winner, highest_bid

bids = {}
choice = True

while choice:
    name = input("what is your name?:")
    price = int(input("what's your bid?: $")) #명령하다, 분부를 내리다
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if should_continue =="no": 
        choice = False
        
    elif should_continue == "yes": # 새로운 창을 띄우는 것처럼 하기위해 강제개행을 20줄 수행 
        print("\n" * 20)

    winner, highest_bid = find_highest_bidder(bids)
    print(f"winner is {winner} with a bid of ${highest_bid}")







#내가 먼저 적어봤었던 코드 
'''
print("Welcom to the secret auction program.")
name = input("what is your name?:")
price = int(input("what's your bid?: $")) #명령하다, 분부를 내리다
should_continue = input("Are there any other bidders? Type 'yes' or 'no'")

True == "no"
if choice == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    after_choice_name = input("What is your name?:")
    after_choice_bid = input(int("what's your bid?:")) #명령하다, 분부를 내리다
    after_choice_choice = input("Are there any other bidders? Type 'yes' or 'no'")
    if after_choice_choice == "no":
        if bid > after_choice_bid :
            print(f"your bid is {bid}. u r win")
        else : 
            print(f"your bid is {after_choice_bid}. u r win")

#Auction = {"person_name" : "bidding_price"}

#for i in Auction:
'''



=======
#비밀경매 프로그램과 순서도

'''
사람의 이름 = 키
입찰가 = Value

마지막에 모든 사람이 입찰 마칠시
그 딕셔너리 반복해서 누가 가장 높은 입찰했는지 알아내야함
'''

print("Welcom to the secret auction program.")
name = input("what is your name?:")
price = int(input("what's your bid?: $")) #명령하다, 분부를 내리다
should_continue = input("Are there any other bidders? Type 'yes' or 'no'")

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0 #최고 입찰가
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder 
    return winner, highest_bid

bids = {}
choice = True

while choice:
    name = input("what is your name?:")
    price = int(input("what's your bid?: $")) #명령하다, 분부를 내리다
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if should_continue =="no": 
        choice = False
        
    elif should_continue == "yes": # 새로운 창을 띄우는 것처럼 하기위해 강제개행을 20줄 수행 
        print("\n" * 20)

    winner, highest_bid = find_highest_bidder(bids)
    print(f"winner is {winner} with a bid of ${highest_bid}")







#내가 먼저 적어봤었던 코드 
'''
print("Welcom to the secret auction program.")
name = input("what is your name?:")
price = int(input("what's your bid?: $")) #명령하다, 분부를 내리다
should_continue = input("Are there any other bidders? Type 'yes' or 'no'")

True == "no"
if choice == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    after_choice_name = input("What is your name?:")
    after_choice_bid = input(int("what's your bid?:")) #명령하다, 분부를 내리다
    after_choice_choice = input("Are there any other bidders? Type 'yes' or 'no'")
    if after_choice_choice == "no":
        if bid > after_choice_bid :
            print(f"your bid is {bid}. u r win")
        else : 
            print(f"your bid is {after_choice_bid}. u r win")

#Auction = {"person_name" : "bidding_price"}

#for i in Auction:
'''



>>>>>>> 5869b6b (	new file:   python_practice/ch10/calculator_240908.py)
