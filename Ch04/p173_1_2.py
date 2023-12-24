'''
반복적으로 3과목 점수 입력
점수 모두 0일 경우 프로그램 종료
......?
'''
sub=0
sum=0
cnt=1
avg=0

while True :
    sub1=(int(input("첫 번째 과목 점수 입력:")))
    sub2=(int(input("두 번째 과목 점수 입력:")))
    sub3=(int(input("세 번째 과목 점수 입력:")))

    if (sub1 and sub2 and sub3>0) :
        sum=sub1+sub2+sub3
        avg=sum/3
    print("총점 {}점, 평균 {}점".format(sum,avg))

    if sub==0 :
        break
    print('총'+str(cnt)+'명의 성적 처리 하였습니다.')