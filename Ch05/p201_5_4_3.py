'''
0429 랜덤모듈
'''
import random #랜덤모듈 추가

list1=[] #빈 리스트 생성

for i in range(10) : #10번 반복
    list1.append(random.randint(1,100))

print(list1)