'''
숫자를 입력 받아 그 수 만큼
*을 하나씩 증가하여 출력
'''

num=int(input("숫자 입력 :"))

for i in range (1,num+1) : #줄반복
    for j in range (1, i+1) : #*반복
        print("*",end=' ')
        j=1+j
    print() #줄바꿈
    i=1+i    