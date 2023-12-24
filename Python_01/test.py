# 파이썬은 타입 지정 안함, 적힌 내용으로 자동 지정되는 듯
#1. list/for문
"""
family = ["할아버지", "할머니", "누나", "동생"]
i=0

while ( i < len(family)) :
    print("우리 가족에는", family[i], "이/가 있습니다.")
    i = i+1
"""
#2. for 사용. 생각해보기
"""
a=10
for i in range(5) :
    a-=1
    if a==7:
        break;
    print("a = ", a, ", i = ", i)

"""
#3. while문
"""
i=1
sum = 0

while  i < 11  : # i가 10이하일 때 반복
    sum = sum + i
    i = i + 1
    if ( i == 11) :
        print(" 1부터 10까지의 합 : ", sum)
"""
#4. 비밀번호
"""       
password = "" #공백

while password != "1234" : # 1234가 아닐 때 반복
    password = input("암호 입력 : ")
    
print("Login success!")
"""
#5. while 무한반복
"""
while True :
    n = int(input("숫자 입력 >> "))
    if n == 9 :
        print("종료5")
        break
    print("입력한 숫자 : ", n)
"""
#6. 구구단

n = int(input("숫자 입력 >> "))
for i in range(1, 10) : # 1부터 9까지 반복
    value = n * i
    print(n , " * ", i, " = ", value)