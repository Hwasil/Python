'''
0526
입력한 두 정수 사이의 정수합 오류
'''

#함수
def allSum(a,b) :
    for i in range(a,b+1) :
        sum=0
        sum=sum+i
        i=i+1
    return sum

#메인 프로그램
a=int(input("첫 번째 숫자 : "))
b=int(input("두 번째 숫자 : "))

sum=allSum(a,b)

print("입력한 두 정수 사이의 정수합 : ",sum)