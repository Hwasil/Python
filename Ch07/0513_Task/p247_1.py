'''
0513 과제
num.txt(프로그램에서 자동 생성), avg.txt(프로그램에서 생성)
'''

num=[] 
import random

for i in range(30) :
    num.append(random.randint(1,100))
    
f=open("D:\\Python_EX\\0513\\num.txt",'w')

f.writelines(num)

f.close()

# 평균 계산 후 파일 생성
f=open("D:\\Python_EX\\0513\\num.txt",'r')
lines=f.readlines()

for num in lines :
    scorelist=num.split()

    sum=0

    for i in range(0,5) :
        sum=sum+int(scorelist[i])
    
    for j in range(1,6) :
        j=j+1
    
    print(j+"번째 학생의 평균 : ",sum/5)

f.close()