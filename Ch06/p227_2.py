'''
p227-2
2,3,7 각각의 배수의 집합과 모두의 배수를 집합으로 출력
띄어쓰기 블록?
'''
num=int(input('숫자를 입력 :'))
t1=set()
t2=set()
t3=set()
t4=set()


for i in range(1,num+1,2) :
    if i%2==0 :
    t1.add(i,end=',')
print("2의 배수 :",t1)

for i in range(1,num+1,3) :
    if i%3==0 :
    t2.add(i,end=',')
print("3의 배수 :",t2)

for i in range(1,num+1,7) :
    if i%7==0 :
    t3.add(i,end=',')
print("7의 배수 :",t3)

for i in range(1,num+1,42) :
    if i%42==0 :
    t4.add(i,end=',')
print("2,3,7의 배수 :",t4)
    

    