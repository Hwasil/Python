'''
0526
p.268 모듈 만들기
'''

pi=3.1415 #상수

#함수 선언
def rectangleArea(width,depth) : #사각형의 넓이
    return width*depth

def triangleArea(base, height) : #삼각형의 넓이
    return base*height/2

def circleArea(r) : #원의 넓이
    return pi*r*r

def circumference(r) : #원의 둘레
    return 2*pi*r
