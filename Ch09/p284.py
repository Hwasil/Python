'''
0608
class 만들기
'''

class PlusMinus : #클래스 생성
    def plusminus(self,x,y) : #속성
        self.sum=x+y
        self.minus=x-y

    def result(self) : # 반환 시켜주는 기능만
        return self.sum, self.minus

# 메인
x=int(input("첫 번째 숫자:"))
y=int(input("두 번째 숫자:"))

# 객체 생성
pm=PlusMinus() # class를 만들기 위한 객체 생성 -> class 이름(기능과 메소드를 상속(=사용))
pm.plusminus(x,y) # class PlusMinus의 plusmiuns메소드 사용(호출)
a,b=pm.result() # 결과 반환

print("입력한 두 수의 합 :",a)
print("입력한 두 수의 차 :",b)