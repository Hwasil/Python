'''
소수 여부 판단
break문 사용
'''
num=int(input("숫자 입력:"))

for i in range (2, num) :
    if num%i==0 :
        print("소수가 아닙니다.")
        break
    
else :
    print("소수 입니다.")

print("소수 판별 프로그램을 이용해주셔서 감사합니다.")
    
