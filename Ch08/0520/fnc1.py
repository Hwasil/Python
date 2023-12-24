'''
0520
함수 정의와 함수 호출
'''

#사용자 정의 함수
def bigsmall(a,b) : #함수 정의
    if a>b : #함수 몸통
        big = a
        small = b
    else :
        big=b
        small=a
    return big, small #함수의 결과를 주프로그램에 반환

# 주 프로그램 
num1=int(input("첫 번째 숫자 : "))
num2=int(input("두 번째 숫자 : "))

x,y=bigsmall(num1,num2) # 함수 호출 # 함수 결과를 x,y에 저장 / return 받음

print("큰 수 :",x)
print("작은 수 :",y)

