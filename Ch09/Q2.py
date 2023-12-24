'''
0610
문제2 
암호 입력 받아 인증 처리하는 프로그램
(암호 admine)
'''

pw_pass='admine' #비밀번호
i=0

while True :
    pw=input('패스워드 입력 :')
    if pw!=pw_pass :
        print('암호가 틀립니다.')
        i=i+1

    if i==3 :
        print('시도횟수 초과')
        break 

    elif pw==pw_pass :
        print('환영합니다.')
        break