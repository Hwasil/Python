'''입력한 숫자의 배수만을 더한다'''
multi=int(input('합을 원하는 배수 입력:'))
sum=0

for i in range (multi,1001,multi) :
    sum=sum+i

print("1부터 1000까지의 {}배수의 합은:{}".format(multi,sum))