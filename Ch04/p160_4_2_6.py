'''
2021.04.14
오화실
while/contiune문 사용, 배수의 합계 구하기
'''
num=int(input("숫자 입력:"))
i=0
sum=0

while i<100 :
    i=i+1
    if i%num !=0 :
        continue
    sum=sum+i # 위치 기억!

print('1~100까지의 {}배수 합은 : {}'.format(num, sum))