'''
0526 과제
'''

# 메인 프로그램
import find
  
a=int(input("첫 번째 숫자 : "))
b=int(input("두 번째 숫자 : "))
c=int(input("세 번째 숫자 : "))

print("가장 큰 수 (findMax()) : ",find.findMax(a,b,c)) #모듈 호출
print("가장 작은 수 (findMin()) : ",find.findMin(a,b,c))
print("숫자의 합 (findSum()) : ",find.findSum(a,b,c))