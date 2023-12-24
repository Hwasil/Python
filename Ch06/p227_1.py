'''
p227-1
max(), min() 사용 불가능 -> 다른 방법 찾기
'''
import random 
num=set()

for i in range(10) :
    num.add(random.randint(1,100))

print("생성된 집합 :",num)
print("집합에서 가장 큰 수 :",max(num))
print("집합에서 가장 작은 수 :",min(num))