"""급여 구하기(0325) 오화실
다른 방법"""
sal=3000000 #본봉
extra_sal=300000 #수당
tax=int(sal+extra_sal)*0.2 #세금
total_sal=sal+extra_sal-tax #총수령액

print("홍길동의 이번달 수령액은:",total_sal)