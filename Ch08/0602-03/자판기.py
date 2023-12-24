'''
2021.06.03
차유정
'''
#메뉴와 가격 출력
def sell_menu():
    print("** 자판기 판매 메뉴 **")
    for i in range(0,5):
        print(i+1,":",manu[i],price[i])

#음료 잔액 반환
def drink():
    global money
    while True:
        choice=int(input("메뉴 선택(종료:0):"))
        if money<400:
            print("잔액부족")
        elif choice==1:
            print("콜라 구입완료")
            money=money-price[0]
            print("잔액:",money)
        elif choice==2:
            print("사이다 구입완료")
            money=money-price[1]
            print("잔액:",money)
        elif choice==3:
            print("환타 구입완료")
            money=money-price[2]
            print("잔액:",money)
        elif choice==4:
            print("커피 구입완료")
            money=money-price[3]
            print("잔액:",money)
        elif choice==5:
            print("생수 구입완료")
            money=money-price[4]
            print("잔액:",money)
        elif choice==0:
            print("자판기 종료")
            break
        
#최종잔액 동전으로 교환
def change():
    global money
    c1_money=money//500
    money=money%500
    print("coin500:",c1_money,"개 반환")
    c5_money=money//100
    money=money%100
    print("coin100:",c5_money,"개 반환")
    print("나머지:",money,"반환")

manu=["콜라","사이다","환타","커피","생수"]
price=[500,500,600,600,400]
m=sell_menu()
money=int(input("돈을 투입하세요: "))
d=drink()
print()
c=change()