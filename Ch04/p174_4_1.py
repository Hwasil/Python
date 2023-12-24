'''
1부터 100까지의 합
while 반복문
10을 기준으로 합계 출력
p174-4 다른 방법으로 시도 -> 10단위로 끊는 것 못하겠다.
'''
i=1
sum=0

while True :
    sum=sum+i
    i=i+1  
    if i>=101 :
        break  
print("1-100:",sum)
    