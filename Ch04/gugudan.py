'''
21.04.21
구구단 전체 출력
'''

for i in range (2,10) :
    print("**",i,"**")
    for j in range(1,10):
        mul=i*j
        if mul%2==0 : #계산 결과가 짝수인 것만 출력
            print(i,"*",j,"=",mul)