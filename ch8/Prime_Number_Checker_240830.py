#소수 계산기 만들기
#prime_number_checker


def prime_checker(number):
    is_prime = True
    for i in range(2, number): #소수는 자기자신과 1로 나누어 떨어지는 수 이기 때문에 2부터 넣는다. 
        is_prime = False
    
    if is_prime: #소수인 경우
        print("It's a prime number.")
    else: #소수가 아닌경우
        print("It's not a prime number.")

n = int(input()) 
prime_checker(number=n)
