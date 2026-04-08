### 문자열 자료형 (string)

# a = "hello world"
"""print(len(a))  # 공백까지 카운팅
print(a[6])
print(a[0:4:2])
print(a[0:3] + a[5:7])"""

# 포맷팅
""" s = 50
s1 = "coding"
s2 = "!!" 
print("hello" + "coding" + "world")
print("hello %s world" % "coding") 
print("hello %s world%s" % (s1, s2))

# print("hello" + 30 + "world") : error
print("hello %d world" % s)
print("hello {0} world {1}".format(60, "meow"))
print(f"hello {s1} world")

print("hello", 30, "world")
print("hello", s1, "world", s2) """

#
""" s = "  hh_heeee_llow  "
print(s.count("h"))
print(s.index("h"))  # 맨 앞에 값 인덱스만 출력
print(s.find("s"))  # 값을 못 찾으면 -1 출력

# 대소문자 변경 : 결과값 전달 <-> lower
print(s.upper()) 

# 공백 삭제
# 양쪽 : strip,  왼쪽 : lstrip, 오른쪽 : rstrip
sNew = s.lstrip()
print(sNew)

# 잘려서 리스트로 출력
sNew = s.split("_")  # 값이 없거나 " "이면 공백이 기준
print(sNew)

num = 123
s_num = "123" """

### 조건문 (들여쓰기 : tab 1, space 4)
# 조건이 ture 일 때만 실행
""" num = -10

if num > 0:
    print("num is int")
    print("thank you")
print("the end")

# 비교 연산자 : >, >=, <, <=., ==, !=
print(num > 0 and num != 10)
print(num > 0 or num != 10)
print(not num > 0)

c = "H"
if c == "H":
    print("the letter is H")
print("end")

# 리스트 안에 값이 있으면 true, 없으면 false
s = [1, 2, 3]
print(7 not in s)

s1 = "hello"
print("p" in s1) """

# id == 메모리 주소 : 저장된 위치와 비슷
a = [1, 2, 3]
b = a # a와 b의 가리키는 id가 같음
print(id(a))
print(id(b))
print(a is b)

b = a.copy()  # a를 복사한 b라는 새로운 리스트
b.append(4)
print(a)
print(b)
