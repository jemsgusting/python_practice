
def add(n1,n2): #더하기
    return n1+n2
def sub(n1,n2): #빼기
    return n1-n2
def multiply(n1,n2): #곱하기
    return n1*n2
def divide(n1,n2): #나누기
    return n1/n2

operations = {
            "+" : add,
            "-" : sub,
            "*" : multiply,
            "/" : divide,
        }

def calculator():
    should_accumulate = True
    n1 = float(input("what's the first number?:"))

    while should_accumulate:
        for choiced_symbol in operations:
            print(choiced_symbol)
        operation_choice= input("Pick an operation:")
        n2 = float(input("what's the next number?:"))
        result = (operations[operation_choice](n1,n2)) #입력값에 대한 계산 수행
        print(f"{n1} {operation_choice} {n2} = {result}") 
        continue_check = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation : y ")

        if continue_check == 'y':
            n1 = result
        else :
            False
            print("\n" * 20)
            calculator()


calculator()


