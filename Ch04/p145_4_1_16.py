"""복합 조건 프로그램"""
grade=int(input('직급:'))
age=int(input('나이:'))

if (grade==7 or grade==8) and (40<=age<=49) :
    print('연금 80% 대상자입니다.')

elif (grade==5 or grade==6) and (50<=age<=59) :
     print('연금 100% 대상자입니다.')

else :
    print('연금 대상자가 아닙니다.')
