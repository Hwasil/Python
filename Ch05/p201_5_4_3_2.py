'''
0429 
랜덤모듈 사용, 함수와 리스트 객체 메소드 사용
'''
import random #랜덤모듈 추가

list1=[] #빈 리스트 생성

for i in range(10) : #10번 반복
    list1.append(random.randint(1,100))

print("생성된 리스트:",list1)
print("가장 큰 값:",max(list1))
print("가장 작은 값:",min(list1))
print("전체 요소의 합:",sum(list1))
list1.sort()
print("정렬된 리스트:",list1)