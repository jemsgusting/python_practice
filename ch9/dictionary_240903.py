<<<<<<< HEAD
# 파이썬 딕셔너리

'''
만약 사전에서 code라는 단어를 찾으면 명령어와 같은 정의를 찾을 수 이씅ㅁ
그리고 딕셔너리는 관련 정보를 그룹화하고 태그를 달 수 있는 유용한 장점이 ㅣㅇㅆ음
딕셔너리를 표 형태로 생각함
모든 딕셔너리는 두 분류로함
왼쪽은 키 = 사전의 단어에 해당
value = 관련된값 , 단어의 실제 정의에 해당

딕셔너리의 끝에 도달할때 까지 키와 value 를 계속 ㅜㅊ가가능
'''

#{key:value} 꼴이다
#사전처럼 key 자리에 단어의 이름을 쓰고 value 자리에 해당 단어의 설명을 기입하면됨
#아래가 형식

programming_dictionary = {
    "bug":  "an error i na program that prevents the program from running as expected ",
    "function" : "a piece of code that you cna easily cll over and over again"    
}

print(programming_dictionary["bug"]) # bug의 value 출력
programming_dictionary["loop"] = "the action of doing something over and over again" # 딕셔너리에 추가한것 


print(programming_dictionary)
# 필요시에 {} 안을 지우고 싶을때 programming_dictionary = {} 다음에 print를 놓는다.



programming_dictionary["bug"] = "a moth in your computer" # bug 뜻 재정의


for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
=======
# 파이썬 딕셔너리

'''
만약 사전에서 code라는 단어를 찾으면 명령어와 같은 정의를 찾을 수 이씅ㅁ
그리고 딕셔너리는 관련 정보를 그룹화하고 태그를 달 수 있는 유용한 장점이 ㅣㅇㅆ음
딕셔너리를 표 형태로 생각함
모든 딕셔너리는 두 분류로함
왼쪽은 키 = 사전의 단어에 해당
value = 관련된값 , 단어의 실제 정의에 해당

딕셔너리의 끝에 도달할때 까지 키와 value 를 계속 ㅜㅊ가가능
'''

#{key:value} 꼴이다
#사전처럼 key 자리에 단어의 이름을 쓰고 value 자리에 해당 단어의 설명을 기입하면됨
#아래가 형식

programming_dictionary = {
    "bug":  "an error i na program that prevents the program from running as expected ",
    "function" : "a piece of code that you cna easily cll over and over again"    
}

print(programming_dictionary["bug"]) # bug의 value 출력
programming_dictionary["loop"] = "the action of doing something over and over again" # 딕셔너리에 추가한것 


print(programming_dictionary)
# 필요시에 {} 안을 지우고 싶을때 programming_dictionary = {} 다음에 print를 놓는다.



programming_dictionary["bug"] = "a moth in your computer" # bug 뜻 재정의


for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
>>>>>>> 5869b6b (	new file:   python_practice/ch10/calculator_240908.py)
    