'''
숫자를 입력 받아 그 수 만큼
*을 하나씩 감소하여 출력
(문제변형)
'''

num=int(input("숫자 입력 :"))

for i in range(num,0,-1) : #줄반복
    for j in range (i,0,-1) : #*반복
        print("*",end=' ')
        j=j+1
    print() #줄바꿈
    i=i+1 #+,- 상관 없는 이유???