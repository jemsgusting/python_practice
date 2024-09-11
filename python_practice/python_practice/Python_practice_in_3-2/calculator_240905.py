'''
def format_name(f_name, l_name):
    #괄호 안에 f_name, l_name를 쓴 것은 두 매개변수로부터 입력받는다는 의미이다.
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
        
print(format_name(f_name= "Angela", l_name= "ANGELA"))
'''

#def 함수의 () 괄호 안에 들어가는 변수는 입력을 허용하는 함수이다.
#입력에 따라 함수코드를 수정하고 매번 다른 작업 수행가능
#이후에 함수가 완료되면 출력을 가질 수 있다.
#입력과 출력은 완전히 별개 





def function_1(text): 
    return text + text

def function_2(text):
    return text.title() #title()을 사용하면 첫글자는 대문자 , 나머지는 소문자로 만듦

output = function_2(function_1("hello"))
print(output) 
# 한 함수의 출력을 다른 함수의 입력으로 변경한것 ! 
