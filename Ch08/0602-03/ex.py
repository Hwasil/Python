#가위 바위 보 게임
import random
list1=['가위','바위','보']

def Game(com,human):
    com=0
    human=0

    while True:
        a=(input("가위,바위,보 입력:"))
        b=random.randint(list1.index('가위'),list1.index('보'))#1:가위 2:바위 3:보
        if a==list1[0]:
            if b==0:
                print("컴퓨터:가위")
                print("비김")
            elif b==1:
                print("컴퓨터:바위")
                print("컴퓨터 승")
                com=com+1
            elif b==2:
                print("컴퓨터:보")
                print("사람 승")
                human=human+1
        elif a==list1[1]:
            if b==0:
                print("컴퓨터:가위")
                print("사람 승")
                human=human+1
            elif b==1:
                print("컴퓨터:바위")
                print("비김")
            elif b==2:
                print("컴퓨터:보")
                print("컴퓨터 승")
                com=com+1
        elif a==list1[2]:
            if b==0:
                print("컴퓨터:가위")
                print("컴퓨터 승")
                com=com+1
            elif b==1:
                print("컴퓨터:바위")
                print("사람 승")
                human=human+1
            elif b==2:
                print("컴퓨터:보")
                print("비김")
        elif a=="":
            print("입력오류")
        if com==3 or human==3:
            break
    if com==3:
        print("컴퓨터 승!")
        return com
    else:
        print("사람 승!")
        return human

com=human=Game(0,0)