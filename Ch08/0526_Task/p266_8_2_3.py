'''
0526
'<=' not supported between instances of 'list' and 'int'
'''

#함수
list=[] 

def findprime(a,b) :
    for i in range (a,b+1) :
        for j in range(1,i+1) :
            if i%j==0 :
                list.append(i) #약수를 리스트에 추가
    return list


#메인 프로그램
a=int(input("첫 번째 숫자 : "))
b=int(input("두 번째 숫자 : "))

list=findprime(a,b)

if len(list)==2 :
    print("두 숫자 사이의 소수 : ",list)
    print("소수의 개수 : ",)