'''
0602
가위바위보 게임
오류 1
'''

#함수

def Game(com,human) :
    com1=0 # 가위바위보는 반복하지만 여기에서 변수 값이 초기화 되서 2로 넘어가지 않음
    human1=0

    if com==1 : #가위
        if human=='가위' :
            print("비김")
        elif human=='바위' :
            human1 += 1
            print('사람 승')
        else : 
            com1 += 1
            print('컴퓨터 승')

    elif com==2 : #바위
        if human=='가위' :
            com1 += 1
            print('컴퓨터 승')
        elif human=='바위' :
            print("비김")
        else : 
            human1 += 1
            print('사람 승')

    elif com==3 : #보
        if human=='가위' :
            human1 += 1
            print('사람 승')
        elif human=='바위' :
            com1 += 1
            print('컴퓨터 승')
        else : 
            print("비김")
    else :
        print('입력오류')
    
    return com1, human1

# 메인 프로그램
import random

#list1=['가위','바위','보']

while True :
    #사람 입력 반복
    h_human=input('가위 바위 보 중 입력 :')
    # 컴퓨터 선택 반복
    c_com=random.randint(1,3)
    if c_com==1 :
        print('컴퓨터 : 가위')
    elif c_com==2 :
        print('컴퓨터 : 바위')
    else :
        print('컴퓨터 : 보')
 
    com1=human1=Game(c_com,h_human) 

    if com1==3 :
        print('컴퓨터 승!')
    if human1==3 :
        print('사람 승!')
        break