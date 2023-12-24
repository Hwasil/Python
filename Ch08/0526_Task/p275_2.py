'''
0526
name 'a' is not defined
'''

#함수
def gugu(a) :
    dan=0
    for i in range(1,10) :
        dan=a*i
        dansum=dansum+dan
    return dansum

print("==",a,"단==")
print(a,"*",i,"=",dan)

#메인 프로그램
a=int(input("정수 입력 : "))

dansum=gugu(a)
print("구구단 결과의 합 : ",dansum)