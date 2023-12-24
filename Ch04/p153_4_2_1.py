'''
2021.04.08 
입력받은 수 까지의 합계 구하기
'''

# while 반복문
num=int(input('정수 입력:'))
i=1
sum=0

while i<=num :
    sum=sum+i
    i=i+1

print("1부터 {}까지의 합계는 {}이다.".format(num,sum))

# for 반복문
num2=int(input('정수 입력:'))
sum2=0

for i in range (1, num2+1) :
    sum2=sum2+i
    
print("1부터 {}까지의 합계는 {}이다.".format(num2,sum2))