'''다중 if문'''
num1=int(input("첫 번째 숫자 입력:"))
num2=int(input("두 번째 숫자 입력:"))

if (num1%2==0) and (num2%2==0):
    print("두 숫자 모두 짝수.")

elif (num1%2!=0) and (num2%2!=0):
    print("두 숫자 모두 홀수.")

else:
    print("홀수 짝수가 섞여 있다.")
    