# 리스트(List) : 정수, 실수, 문자, 불 형식, 리스트 작성 가능
# 리스트 원소(element), 인덱스(index) : 0부터 시작

a = [1, 0.7, "hello", [4, 5, 6], True]
b = [100, 200, 300]

# 2차원 배열
print(a[3][0])  
print(a[-1][2])


# 리스트 슬라이싱
""" 시작 인덱스 : 마지막 인덱스 -1까지 출력 : 증감값(step) -> 결과값도 리스트
공백 시 처음부터, 끝까지 [1:], [:4], [:], [::2], ***[::-2] 거꾸로 출력 """
print(a[0:4:2])

### 리스트이름.내장함수()

# 리스트이름.append(값) : 리스트 맨 뒤에다가 추가
a.append(100)
print(a)

# 수정 (덮어쓰기)
a[0] = 7
print(a)

## 삭제
del a[1]
print(a)

# 리스트이름.pop(index) : 값을 전달하고 삭제
b = a.pop(1)  
print(a)
print(b)

a.remove(0.7)
print(a)

# 리스트 뒤집기
a.reverse()  
print(a)

# index(값) 값이 리스트에 있으면 인덱스 출력 / 없으면 error
d = a.index(100)
print(d)

# 인덱스 0에 값을 삽입
a.insert(0, "meow")
print(a)

#
c = a.count("hello")
print(c)


### 리스트 2개
# print(a + b)  # 물리적으로 붙는 건 아님
a.extend(b)  # 실제로도 붙음
print(a)

c = a.copy()
d = a[:]
print(c)
print(d)

e = a + b
print(e)
print(e[5])

# 리스트 길이 = 리스트 안 원소 개수
print(len(a))

# 정렬 (default : 오름차순, reverse=True : 내림차순) => only num
a.sort(reverse=True)
print(a)
