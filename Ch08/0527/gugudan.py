'''
0527
p275 2번 feedback
구구단 출력
'''

#함수 정의
def gugudan(dan) :
    gugu_hap=0
    for i in range (1,10) :
        print(dan,"*",i,'=',dan*i)
        gugu_hap += dan*i
    return gugu_hap

#메인 프로그램
num1=int(input("출력할 단 입력 :"))

res_return=gugudan(num1)

print('구구단 결과의 합 : ',res_return)