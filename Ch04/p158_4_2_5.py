'''팩토리얼을 구하는 프로그램, for문'''
num=int(input('팩토리얼 구하는 숫자:'))
times=1

for i in range (num,0,-1) :
    times=times*i

print('{}의 팩토리얼 값은 : {}'.format(num,times))