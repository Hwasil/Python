'''
10개의 숫자 입력
짝수 번째 숫자 양수는 음수로, 음수는 양수로 바꾸어 합 구하기
'''
cnt=1 # 입력받는 숫자 갯수, 짝수 번째 찾기
sum=0

while (cnt<=10) :
    num=int(input("숫자 입력:"))
    if cnt%2==0 :
        num=num*-1
    sum=sum+num
    cnt=cnt+1 #주의

print("합계:",sum)