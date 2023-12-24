"""이중 if문"""
num=int(input('숫자 입력:'))

if num>0 :
    print('입력값 {}은 양수입니다.'.format(num))

elif num==0 :
    print('입력값 {}은 0입니다.'.format(num))

else :
    print('입력값 {}은 음수입니다.'.format(num))