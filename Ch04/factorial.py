'''
0421 
팩토리얼 계산
'''
num=int(input("숫자 입력:"))
fac=1

for i in range(num,0,-1) :
    fac=fac*i

print(num,"까지의 팩토리얼 계산 결과:",fac)