'''
2021.04.14
4장 연습문제 3
'''
i=0
sum=0
cnt=1 

while True :
    num=int(input(str(cnt)+"번째 숫자 입력:"))

    if num>0 :
        sum=sum+num
        cnt=cnt+1
    if cnt>10 :
        break

avg=sum/(cnt-1) # 1을 빼는 이유 찾기

print("숫자 10개의 합계 :",sum)
print("숫자 10개의 평균 :",avg)