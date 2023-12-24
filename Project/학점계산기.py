'''
팀프로젝트(기말)
학점 계산기
''' 

list1=[] # 빈 리스트 - 강좌명
list2=[] # 학점
list3=[] # 등급(점수)

# 새 텍스트 파일 불러와서 작성
sub_jumsu=open("D:\\Python_EX\\팀프로젝트\\학생 입력.txt","w")

while True:
    # 입력한 내용을 리스트에 넣기
    a=input("과목을 입력:")
    list1.append(a)

    b=input("학점을 입력:")
    list2.append(b) 

    c=input("등급을 입력:")
    if c=='A'or c=='A+' or c=='B' or c=='B+' or c=='C'or c=='C+'or c=='D'or c=='D+' or c=='F':
        list3.append(c)

    # 입력된 등급이 잘못 입력되었다면 list1, list2의 내용 삭제
    else:
        print("등급이 잘못 입력 되었습니다")
        list1.pop()
        list2.pop()

    # list3의 요소의 갯수가 3이라면 종료
    if len(list3)==3:
        break

a=' '.join(list1)
b=' '.join(list2)
c=' '.join(list3)

sub_jumsu.write(a+"\n")
sub_jumsu.write(b+"\n")
sub_jumsu.write(c+"\n")

sub_jumsu.close()

# 작성한 텍스트 파일 읽어오기
sub_jumsu=open("D:\\Python_EX\\팀프로젝트\\학생 입력.txt","r")

list4=[] # 한 과목 당 학점과 (등급 기준표에 따라 환산한)등급 점수의 곱을 넣을 빈리스트

# 등급 환산표에 따라 등급을 변환하여 계산
for i in range(1,4):
    if list3[i-1]=='A+':
        a=int(list2[i-1])*4.5

    elif list3[i-1]=='A':
        a=int(list2[i-1])*4

    elif list3[i-1]=='B+':
        a=int(list2[i-1])*3.5

    elif list3[i-1]=='B':
        a=int(list2[i-1])*3

    elif list3[i-1]=='C+':
        a=int(list2[i-1])*2.5

    elif list3[i-1]=='C':
        a=int(list2[i-1])*2

    elif list3[i-1]=='D+':
        a=int(list2[i-1])*1.5

    elif list3[i-1]=='D':
        a=int(list2[i-1])*1

    elif list3[i-1]=='F':
        a=int(list2[i-1])*0
    list4.append(a)

# 평균 계산
average=(list4[0]+list4[1]+list4[2])/(int(list2[0])+int(list2[1])+int(list2[2]))
sub_jumsu.close()

# 학점 평균 계산 결과 새 파일에 입력
sub_jumsu=open("D:\\Python_EX\\팀프로젝트\\학점 평균.txt","w")

sub_jumsu.write(str(average))
print("학점 평균은",average)

sub_jumsu.close()