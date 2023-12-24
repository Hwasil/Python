'''
0609
Box() class 작성 -> 생성자 메소드 활용 (과제)
'''

class Box() :

    def __init__(self,width=1,depth=1,height=1) :
        self.vol=width*depth*height #부피 구하기
         

    def result(self) :
        return self.width, self.depth, self.height, self.vol

b1=Box() # 객체 생성
b2=Box()
b3=Box()
b4=Box()


w,d,h,v=b1.result()
print('가로 :',w,'세로 :',d,'높이 :',h,'부피 :',v)

w,d,h,v=b2.result(10)
print('가로 :',w,'세로 :',d,'높이 :',h,'부피 :',v)

w,d,h,v=b3.result(10,20)
print('가로 :',w,'세로 :',d,'높이 :',h,'부피 :',v)

w,d,h,v=b4.result(10,20,30)
print('가로 :',w,'세로 :',d,'높이 :',h,'부피 :',v)