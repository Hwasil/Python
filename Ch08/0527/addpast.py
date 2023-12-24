'''
0527
add 함수 활용
'''

import add

num1=int(input("첫 번째 숫자 입력 : "))
num2=int(input("두 번째 숫자 입력 : "))

res=add.add(num1,num2)  #add 함수 호출 후 결과를 res 변수에 return 받음
   #외부 호출 함수 = 호출 파일.함수이름

print(num1,"+",num2,'=',res)