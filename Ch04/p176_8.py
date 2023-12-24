'''0415'''
num=int(input("숫자 입력 :")) 
cnt=0 #약수의 개수 저장

for i in range (2, num+1) : #2부터 num까지의 중에서 소수 찾기, 1은 소수 아님
    for j in range (1, i+1) : # i의 약수 구하기
        if i%j==0 :
            cnt=cnt+1
    if cnt==2 : 
        print(i,end=' ')
    cnt=0 # cnt변수 초기화