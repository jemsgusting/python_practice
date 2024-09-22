<<<<<<< HEAD
#딕셔너리와 리스트 동시 사용 예제

capital = {
    "france" : "paris",
    "germany" : "berlin"
}

'''
travel_log = {
    #프랑스의 경우 key가 france , value를 리스트 하나로 만듦
    "france" : ["paris", "Lille", "Dijon"],
    "germany" : ["stuttgart", "berlin"],
}


print(travel_log)
print(travel_log["france"])
print(travel_log["france"][0])
'''

nested_list = ["A","B",["C","D"]]

#print(nested_list[2][1])

travel_log = {
    "France" : {
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visited" : 8
    }, 
    "Germany" : {
        "citied_visited" : ["stuttgart", "berlin"],
        "total_visited" : 8
    } 
}

#print(travel_log)
=======
#딕셔너리와 리스트 동시 사용 예제

capital = {
    "france" : "paris",
    "germany" : "berlin"
}

'''
travel_log = {
    #프랑스의 경우 key가 france , value를 리스트 하나로 만듦
    "france" : ["paris", "Lille", "Dijon"],
    "germany" : ["stuttgart", "berlin"],
}


print(travel_log)
print(travel_log["france"])
print(travel_log["france"][0])
'''

nested_list = ["A","B",["C","D"]]

#print(nested_list[2][1])

travel_log = {
    "France" : {
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visited" : 8
    }, 
    "Germany" : {
        "citied_visited" : ["stuttgart", "berlin"],
        "total_visited" : 8
    } 
}

#print(travel_log)
>>>>>>> 5869b6b (	new file:   python_practice/ch10/calculator_240908.py)
print(travel_log["Germany"]["citied_visited"][1])