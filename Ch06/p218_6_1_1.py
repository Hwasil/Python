'''
21.05.06
'''

import random
num1=set()
num2=set()

while True :
    if len(num1)<10 : #num1집합에 랜덤 수 10개 추가
        num1.add(random.randint(1,100))

    if len(num2)<10 : #num2집합에 랜덤 수 10개 추가
        num2.add(random.randint(1,100))
    
    if len(num1)==10 and len(num2)==10 :
        break

print("num1의 랜덤 수 :",num1)
print("num2의 랜덤 수 :",num2)
print("num1,num2의 합집합 :",num1.union(num2))
print("num1,num2의 교집합 :",num1.intersection(num2))
print("num1,num2의 차집합 :",num1.difference(num2))