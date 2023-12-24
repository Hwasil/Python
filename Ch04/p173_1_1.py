'''수정 173-1'''
cnt=0 # 성적 처리한 학생 수

while True :
    sub1=int(input("국어 성적:"))
    sub2=int(input("영어 성적:"))
    sub3=int(input("수학 성적:"))

    total=sub1+sub2+sub3 #3과목 촉점
    if total==0 : #반복 종료
        break
    avg=total/3 #세과목 평균
    cnt=cnt+1 

    print(cnt,"번째 학생: 총점",total,"평균:",'%.1f'%avg) 
    # 학생별 총점, 평균
print("총",cnt,"명의 성적 처리") #전체 성적처리 학생