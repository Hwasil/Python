'''
p209-3
1~1000사이의 소수를 구하여 리스트에 저장
소수와 소수의 개수를 출력
소수=float
'''
import random

num=[]

for i in range(10) : 
    num.append(random.randfloat(1,1000))
print(num)