
def greet():
    print("Hello jemin")
    print("How do you do?")
    print("isn't the weather nice today?")

greet()
#write 3 print statements inside the function the greet fuction and run your code

print("________________________")

def greet_with_name(name,name2):
    print(f"Hello {name}")
    print(f"my name is {name2}")

greet_with_name("angela","jemin")


'''
parameter(매개변수) = 함수에 전달된 데이터의 이름
argument =  그 데이터의 실제 값
위의 예제에서는 name이 매개변수가 되고 그 안의 데이터의 실제값이 argument(인자) 이다 
name이 매개변수가 되고 angela, jemin이 인수가 되는 것
'''
print("________________________")
def greet_with(name,location):
    print(f"hello {name}")
    print(f"my house which is {location} ")

greet_with(f"jemin","cheongna")