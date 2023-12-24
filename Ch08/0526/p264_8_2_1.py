'''
0526
3개의 숫자를 매개변수로 받아서 가장큰 수를 반환
findmax(a,b,c) 함수 작성
'''

#함수 정의
def findmax(a, b, c) :
    if a>b :
        biggest=a
    else :
        biggest=b

    if biggest<c :
        biggest=c
       
    return biggest

#main 프로그램
num1=int(input("첫 번째 숫자 : "))
num2=int(input("두 번째 숫자 : "))
num3=int(input("세 번째 숫자 : "))


biggest=findmax(num1,num2,num3)

print("가장 큰 수 : ",biggest)