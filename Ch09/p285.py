'''
0609
class 만들기 (생성자 메소드)
'''

class PlusMinus : 
    def __init__(self,x,y) : # 생성자 메소드 (객체 초기화, 자동으로 실행)
        self.sum=x+y
        self.minus=x-y

    def result(self) : 
        return self.sum, self.minus

# 메인
x=int(input("첫 번째 숫자:"))
y=int(input("두 번째 숫자:"))

# 객체 생성
pm=PlusMinus(x,y) # 객체 생성 -> 객체를 초기화 하기 위해 자동 실행

a,b=pm.result() 

print("입력한 두 수의 합 :",a)
print("입력한 두 수의 차 :",b) 