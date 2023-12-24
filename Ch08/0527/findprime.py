'''
0527
p.266 8-2-3
fidnPrime 함수
'''

# 함수 정의
def findPrime(x,y) :
    cnt=0
    num_list=[]
    print(x,'부터',y,'사이의 소수 :',end='')

    for i in range(x,y+1) :
        for j in range(1,i+1) :
            if i%j==0 : 
                cnt=cnt+1
        if cnt==2 :
            num_list.append(i) #소수이면 리스트에 넣기
        cnt=0 #cnt 변수 초기화
    print(num_list) #소수 리스트 출력
    return len(num_list) #소수의 갯수를 반환

#메인 프로그램
num1=int(input("작은 수 입력 : "))
num2=int(input("큰 수 입력 : "))

prime_cnt=findPrime(num1,num2)

print("소수의 갯수 : ",prime_cnt)