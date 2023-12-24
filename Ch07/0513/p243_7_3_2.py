'''
0513 
파일 입출력 - 성적 평균 계산
'''

# 이름 성적 stu.txt에 저장
from os import close, write


f=open("D:\\Python_EX\\0513\\stu.txt",'w')

i=1
while i<=5 :
    score=input("%d번째 학생 이름과 3과목 성적 :"%i)
    f.write(score+"\n")
    i=1+i

f.close()

#stu.txt 파일 읽어서 평균 구하기
f=open("D:\\Python_EX\\0513\\stu.txt",'r')

while True : #stu.txt 파일 한줄 씩 읽어오기
    score=f.readline()

    if score==" " :
        break

    scorelist=score.split() #score 공백을 기준으로 리스트로 변환

    name=scorelist[0] #이름 저장

    sum=0 #합계
    for i in range(1,4) :
        sum=sum+int(scorelist[i])

print(name,"의 평균 점수 :",sum/3)

f.close()