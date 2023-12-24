"""복합 조건 프로그램"""
sub1=int(input("첫 번째 과목 점수:"))
sub2=int(input("두 번째 과목 점수:"))
total=sub1+sub2

if (sub1>=75) and (sub2>=75) :

    if total>=180 :
        print("최우수학생")

    elif total>=160 :
        print("우수학생")

    elif total>=150 :
        print("보통학생")

else:
    print("분발합시다.")
