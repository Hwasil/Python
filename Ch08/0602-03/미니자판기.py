'''
0603
미니자판기
'''

#함수 정의


def cell_menu() :
    print('**자판기 판매 메뉴**')
    for i in range (0,5) :
        print(i+1,':',menu[i],price[i])

def drink() :
    global money # 전역변수
    while True :
        sel=int(input('메뉴선택 (종료:0):')) #1-5번까지 메뉴 선택 번호
        
        if sel==0 : # 입력한 숫자가 0이면
            break

        else :
            print(menu[sel-1],'구입완료') # menu 리스트의 인덱스 번호
            money=money-price[sel-1] # 구매하고 남은 잔액
            print('남은 잔액',money) #남은 잔액 출력

        if money<price[sel-1] : # 구매할 가격 보다 남은 돈이 적으면
            print('잔액 부족')
            break

def change() : 
    print("자판기 종료")
    a500=money//500 #남은 돈의 500원 갯수
    b500=money%500 # 500원을 빼고 남은 수
    print('coin500 :',a500,'개 반환')

    a100=b500//100 #남은 돈에서 100원 갯수
    print('coin100 :',a100,'개 반환')


# 메인
menu=['콜라','사이다','환타','커피','생수']
price=[500,500,600,600,400]

cell_menu()
# 메뉴 입력
money=int(input('돈을 투입하세요:'))
drink()
change()