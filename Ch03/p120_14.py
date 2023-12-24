"""14번 연습문제"""
sub1=int(input("과목1:"))
sub2=int(input("과목2:"))
sub3=int(input("과목3:"))
sub4=int(input("과목4:"))
sub5=int(input("과목5:"))

sum=sub1+sub2+sub3+sub4+sub5
avg=sum/5

print("점수 총점:",sum,end=' ') #두줄 붙이기
print("평균:",'%0.f'%avg)