'''
반복적으로 3과목 점수 입력
점수 모두 0일 경우 프로그램 종료
?-?
'''
sub=0
sum=0
cnt=1

while True :
    sub=(int(input("과목 점수 입력:")))
    if sub>0:
        sum=sum+sub
        avg=sum/3
    print("총점 {}점, 평균 {}점".format(sum,avg))

    if sub==0 :
        break
    print('총'+str(cnt)+'명의 성적 처리 하였습니다.')