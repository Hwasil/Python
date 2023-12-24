'''복합 조건 프로그램'''
num1=int(input("첫 번째 숫자 입력 :"))
op=input("연산자 입력(+,-,*,/):")
num2=int(input("두 번째 숫자 입력 :"))

if (op=='+') :
    print("수식결과",num1,"+",num2,"=",num1+num2)

elif (op=='-') :
    print("수식결과",num1,"-",num2,"=",num1-num2)

elif (op=='*') :
    print("수식결과",num1,"*",num2,"=",num1*num2)
    
elif (op=='/') :
    print("수식결과",num1,"/",num2,"=",'%.2f'%(num1/num2))

else :
    print("연산자가 없음")
