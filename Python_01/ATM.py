import sys

pin = 1122
balance = 0

def get_balance() :                 # 잔액 확인
    global balance                  # 글로벌을 선언해주지 않으면 새로운 전역변수가 되며 초기값은 0, 글로벌을 선언해줘서 동적으로 변화 가능
    print(f"잔액 >> {balance}")     # 고정된 값이 아닌 변화하는 값 출력 
    
def widthdraw() :                   # 인출
    global balance
    amount = int(input("금액 입력 >> "))
    if amount > balance:
        print("잔액이 부족합니다.")
    else : 
        balance = balance - amount
        print(f"{amount}원 인출! 남은 잔액은 {balance}입니다")
    
def deposit() :                     # 저금
    global balance
    amount = int(input("금액 입력 >> "))
    balance = balance + amount
    print(f"저금한 총 잔액 >> {balance}")
    
    
    
    
userpin=int(input("핀 번호 입력 >> "))

if pin != userpin :
    print("잘못된 핀번호")
    sys.exit()

while True :
    query = int(input("1-잔액확인   2-인출   3-저금   4-종료 >> "))
    if query == 1 :
        get_balance()               #함수 호출
    elif query == 2 :
        widthdraw()
    elif query == 3 :
        deposit()
    else :
        print("시스템 종료")
        sys.exit()
        
