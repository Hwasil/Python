'''
0609
다각형의 넓이를 구하는 기능을 클래스 PolyArea로 구현
pi값을 객체의 속성으로 정의
'''

class PolyArea :
    def __init__(self) :
        self.pi=3.14159
    
    def rectangleArea(self,width,depth) :
        return width*depth

    def triangleArea(self,base,height) :
        return base*height/2

    def circleArea(self,r) :
        return self.pi*r*r

    def circum(self,r) :
        return 2*self.pi*r

pa=PolyArea()

print('가로 세로 10인 사각형의 넓이 :',pa.rectangleArea(10,10))
print('밑변 10, 높이 19인 삼각형의 넓이 :',pa.triangleArea(19,10))
print('반지름이 5인 원의 넓이 :',pa.circleArea(5))
print('반지름이 5인 원의 둘레 :',pa.circum(5))