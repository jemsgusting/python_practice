<<<<<<< HEAD
# 페인트 면적 계산기 

import math

def paint_calc(height,width,cover):
    number_of_cans = (height*width)/cover
    round_up_cans = math.ceil(number_of_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

test_h = int(input()) 
test_w = int(input()) 
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

=======
# 페인트 면적 계산기 

import math

def paint_calc(height,width,cover):
    number_of_cans = (height*width)/cover
    round_up_cans = math.ceil(number_of_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

test_h = int(input()) 
test_w = int(input()) 
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

>>>>>>> 5869b6b (	new file:   python_practice/ch10/calculator_240908.py)
