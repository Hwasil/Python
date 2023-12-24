'''
0609
'''

class Box() :
    def volume(self,width=1,depth=1,height=1) :
        vol=width*depth*height #부피 구하기
        return width, depth, height, vol

b1=Box() # 객체 생성

w,d,h,v = b1.volume()
print('가로 :',w,'세로 :',d,'높이 :',h,'부피 :',v)

w,d,h,v = b1.volume(10)
print('가로 :',w,'세로 :',d,'높이 :',h,'부피 :',v)

w,d,h,v = b1.volume(10,20)
print('가로 :',w,'세로 :',d,'높이 :',h,'부피 :',v)

w,d,h,v = b1.volume(10,20,30)
print('가로 :',w,'세로 :',d,'높이 :',h,'부피 :',v)