'''단순 if'''
kor=int(input("국어 점수 입력 :"))
eng=int(input("영어 점수 입력 :"))
math=int(input("수학 점수 입력 :"))

avg=(kor+eng+math)/3 #과목 점수의 평균

if avg>=95:
    print("당신의 평균은" '%.2f'%avg, "점입니다.")
    print("축하합니다. A+입니다.")

print("감사합니다.")
