'''
0429 실습예제 5-3-1
문자열 메소드 연습
'''
ch=input("영어 문장 입력:")

print("입력된 문자 길이:",len(ch)) #함수
print("각 단어의 첫 문자를 대문자로 변환:",ch.title()) #메소드
print("대문자로 변환",ch.upper())
print("a의 갯수:",ch.count('a'))
print("모두 문자로 구성되어 있는가?:",ch.isalpha())
print("모두 숫자로 구성되어 있는가?:",ch.isdigit())
print("모두 대문자로 구성되어 있는가?:",ch.isupper())