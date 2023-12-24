import sys

""" 
id = 'admin' pw = '1234'
사용자로부터 아이디와 비번을 입력 받아 맞으면 '로그인 성공'
둘 중 하나 이상 틀리면 id or pw 대한 오류 메시지 출력
"""

id = 'admin'
pwd = 1234

while True :
    inputID = input("아이디 입력 >> ")
    if (inputID == 'exit') :
        print("시스템 종료")
        sys.exit()
        
    inputPW = input("비밀번호 입력 >> ")
    if (inputID == id and inputPW == pwd) :
        print("로그인 성공")
    elif (inputID != id and inputPW == pwd) :
        print("아이디가 틀렸습니다.")
    elif (inputID == id and inputPW != pwd) :
        print("비밀번호가 틀렸습니다.")
    elif (inputID != id and inputPW != pwd) :
        print("아이디와 비밀번호 모두 틀렸습니다.")
    
    
    



