"""복합 조건 프로그램"""
month=int(input("현재의 월을 입력(정수):"))

if 3<=month<=5 :
    print("봄입니다.")

elif 6<=month<=8 :
    print("여름입니다.")

elif 9<=month<=11 :
    print("가을입니다.")

elif 2<=month<=12 :
    print("겨울입니다.")

else :
    print("잘못된 입력입니다.")