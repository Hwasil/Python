'''
0520
사각형 넓이 구하기, SquarArea(a,b) 함수 정의
'''

# 함수 정의
def SquarArea(a,b) : 
    area=a*b
    return area

# 메인 프로그램
a=int(input("밑변 입력 :"))
b=int(input("높이 입력 :"))

s_area=SquarArea(a,b) #함수 호출

print("사각형의 넓이 : ",s_area)
