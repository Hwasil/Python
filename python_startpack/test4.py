# 26.04.08
### 함수 -> 재사용


"""def say_hi():
    print("Hi")


say_hi()  # 함수 호출


def A2(s):  # s == 매개변수, 파라미터(parameter)
    print(s)


A2("hello world")  # 인자(argument)


def A3(s):
    return s  # 리턴값, 출력값

x = A3("hello world")
print(x)"""

""" def add(x, y) :
    return x + y

x = 10
y = 50
res = add(x, y)
print(res) """


def add(x, y):
    return x + y


def sub(x, y):  # (큰값 - 작은 값) 리턴
    # pass : 함수 완성 x, 코드 실행해보고 싶을 때
    if x > y:
        t = x - y
    else:
        t = y - x
    return t


def mul(x, y):
    return x * y


def bigger(x, y):
    if x > y:
        t = x
    else:
        t = y
    return t


""" x = 10
y = 5
print(add(x, y))
print(sub(x, y))
print(mul(x, y))
print(bigger(x, y))  """

""" while True:
    print("=======Menu=======")
    print("1. add 2. sub 3. mul 4. bigger 5. end")

    menu = int(input("Menu pic : "))
    if menu >= 5 or menu <= 0:
        break

    x = int(input("첫 번째 숫자 : "))
    y = int(input("두 번째 숫자 : "))
    if menu == 1:
        print(add(x, y))
    elif menu == 2:
        print(sub(x, y))
    elif menu == 3:
        print(mul(x, y))
    elif menu == 4:
        print(bigger(x, y)) """

### 파일 입출력
import os

print(os.getcwd())  # 경로를 찾는 방법

""" f = open("new_text.txt", "w")  # f : 파일 존재하지 않으면 새로 만들어서 작성
for i in range(1, 11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)

f.close()  # 파일을 열었으면 닫기 open -> close """

# 파일 읽기
""" f = open("new_text.txt", "r")
lines = f.readlines()
print(type(lines))  # 한번에 읽기 -> 리스트로 읽어옴

for line in lines:  # 문자열로 변환
    print(type(line))

while True:
    line = f.readline()  # 파일을 한 줄씩 읽어옴
    if not line:
        break  # line이 없으면 while문 탈출
    print(line) 
f.close() """

# 파일 추가
""" f = open("new_text.txt", "a")
for i in range(11, 20) :
    data = f"{i}번째 줄입니다. \n"
    f.write(data)
f.close()
    
# f.close() 없이 사용
with open("new_text.txt", "w") as f :
    f.write("My name is ru!") """
