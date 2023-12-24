'''
0520
사각형 넓이 구하기, SquarArea(a,b) 함수 정의
반환값이 없는 함수 : 함수에서 출력
'''

# 함수 정의
def SquarArea(a,b) : 
    area=a*b
    print("사각형의 넓이 :",area) #함수에서 결과 출력
    return 

# 메인 프로그램
a=int(input("밑변 입력 :"))
b=int(input("높이 입력 :"))

SquarArea(a,b) #함수 호출 / 반환값 없음

