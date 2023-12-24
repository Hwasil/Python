'''
두 숫자 사의 홀수값 모두 더하기
'''
num1=int(input("첫 번째 숫자 입력:"))
num2=int(input("두 번째 숫자 입력:"))
sum=0

for i in range(num1,num2+1) :
    if i%2!=0 : # 홀수값
        sum=sum+i

print("두 숫자 사이 홀수값의 합:",sum)