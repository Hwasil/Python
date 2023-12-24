import sys

"""
조건 : 정가 20,000
    1-6세 미만 : 무료
    6-60세 미만 : 20,000
    60세 이상 : 정가의 50%    
"""

price = 20000

while True :
    age = int(input("나이 입력 >> "))
    
    if (age == 999) :
        break
    elif ( age < 6) :
            print("입장료 무료")
    elif ( 6 <= age < 60) :
        print("입장료 : ", price, "원")
    elif ( age >= 60) :
        print("입장료 : ", price*0.5, "원")