'''
210506 
튜플 생성, 리스트 이용, 멤버 유무 검사 연산자인 'in' 사용
'''
num=(1,4,6,5,4,3,2,0,1,2,4,6,7,9,4,0)
print("생성된 튜플:",num)

num_list=[] #빈 리스트 생성

for i in range(len(num)) :
    if num[i] not in num_list : 
        print(num[i],"개수 :",num.count(num[i]))
        num_list.append(num[i])