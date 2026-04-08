# 26.04.07
### 조건문
# num 이 양수면 양수입니다 출력, 음수이면 음수, 0이면 0 출력
"""num = int(input("숫자(정수) 입력 : "))

if num > 0:
    print("양수 입니다.")
elif num < 0:
    print("음수 입니다.")
else:
    print("0 입니다.")"""

# 세 정수 중에서 가장 큰 수를 출력
""" a = int(input("숫자 입력 : "))
b = int(input("숫자 입력 : "))
c = int(input("숫자 입력 : "))

if a > b and a > c:
    print("가장 큰 수 : ", a)
elif b > a and b > c:
    print("가장 큰 수 : ", b)
else:
    print("가장 큰 수 : ", c)
 """
### 반복문 (while/for)
""" num = 1
while num <= 5:
    print(num)
    num += 1

while True:
    num = int(input("input num : "))

    if num == 999:
        break  # 반복 종료
print("탈출") """

# while문으로 1부터 10까지 출력
""" num = 1
while num < 11:
    print("조건문 : ", num)
    num += 1

while True:
    print("무한 반복 : ", num)

    if num >= 10:
        break
    num += 1

i = 0
while i < 10:
    i += 1
    if i % 3 == 0:  # 3의 배수 찾기
        continue  # 아래쪽 코드 실행 x, 다음 반복으로 넘어감 (가장 가까운 반복문 탈출)
    print(i) 
    
i = 2
while i <= 3:
    j = 1
    print(">>>>>", i, "단")
    while j <= 9:
        print(f"{i} x {j} = {i*j}")  # 가독성
        j += 1
    i += 1 """

# 1-10까지 정수 합
""" num = 1
sum = 0
while num <= 10:
    sum += num
    num += 1
print(sum) """

# while - 반복의 횟수가 정해져있지 않으면
# for - 반복의 횟수가 정해져있으면
""" for i in range(1, 10):
    print(i)
 """
# 1-10까지 포함한 수 중에서 짝수만 더해서 출력
""" sum1 = 0
for i in range(1, 11):
    if i % 2 == 0:
        sum1 += i

print("for >> ", sum1)

i = 1
sum2 = 0
while i <= 10:
    if i % 2 == 0:
        sum2 += i
    i += 1

print("while >> ", sum2)

#
s = [10, 20, 30, 40]
x = "hello"
for i in s:  # 리스트에서 원소를 하나씩 뽑아서 i에 대입, 문자열도 가능
    print(i) """

# for문을 이용해  1-10까지 숫자 중에서 3의 배수만 출력
""" for i in range(3, 11, 3):
    print(i)

# 중첩
for i in range(1, 5):
    for j in range(10, 15):
        print(i, j) """

# 딕셔너리 자료형 (사전) dictionary
# key : value 쌍으로
# 키 값은 중복되면 안됨, 값은 중복 가능

""" d["number"] = "010-1234-5678"  # 값 추가
d["age"] = 33  # 값 수정
print(d) """

# 값 가져오기
""" print(d.keys())  # 키 값 가져오기
for k in d.keys():
    print(k)

print(d.values())  # 값만 가져오기
for v in d.values():
    print(v)

for k, v in d.items():  # 키와 값 모두 가져오기
    print(k, v) """

# print(d.get("weight"), "no data")
# print(164 in d.values())
# print(d.get("weight"))

# 요소 삭제
""" x = d.pop("height")
print(type(x), d)

# 모두 삭제
d.clear()  
print(d)

del d["age"]
print(d) """

""" d = {"name": "짱구", "age": 5, "scores": {"kor": 50, "math": 60, "eng": 70}}
d2 = {"name": "철수", "age": 5, "scores": {"kor": 80, "math": 90, "eng": 100}}

print(d["scores"]) """

# 성적 총점 출력, 성적 평균(총점/len(scores)), 80점 이상의 개수 출력 (list)
""" scores = []
for i in range(5):
    score = float(input("점수 입력 : "))
    scores.append(score)
print(scores)

total = sum(scores)
avg = total / len(scores)
print("성적 총점 : ", total, ", 성적 평균 : ", avg)

count = 0
for i in scores:
    if i >= 80:
        count += 1
print("80점 이상 과목 수 : ", count) """

# 총점, 평균, 80점 이상 학생 수 출력 (dic)
scores = {}
for i in range(3):
    name = input("name : ")
    score = int(input("score : "))
    scores[name] = score

print(scores)

total = sum(scores.values())
""" for v in scores.values():
    total += v """

avg = total / len(scores)
print("성적 총점 : ", total, ", 성적 평균 : ", avg)

count = 0
for j in scores.values():
    if j >= 80:
        count += 1
print("80점 이상 과목 수 : ", count)
