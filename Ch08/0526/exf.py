'''
0526
함출 호출 -> 외부 함수 포함하기
'''

# 외부 함수 호출
import BigSmall

# 주 프로그램 
num1=int(input("첫 번째 숫자 : "))
num2=int(input("두 번째 숫자 : "))

x,y= BigSmall.bigsmall(num1,num2) # 함수 호출 # 함수 결과를 x,y에 저장 / return 받음

print("큰 수 :",x)
print("작은 수 :",y)