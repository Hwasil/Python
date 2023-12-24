'''작은 수에서 큰 수 더하기 / while 반복문'''

fir_num=int(input('첫 번째 숫자:')) # 항상 작은 수 
sec_num=int(input('두 번째 숫자:')) # 항상 큰 수

if fir_num > sec_num : #변수 교환 알고리즘 사용
    temp=fir_num
    fir_num=sec_num
    sec_num=temp

print(fir_num,'부터',sec_num,'까지의 합계:',end='')

sum=0
while fir_num<=sec_num :
    sum=sum+fir_num
    fir_num=fir_num+1

print(sum)