'''
0429 5-4-1
'''
num=[[11,33,22,7],[77,2,90],[3,66,44,9,8]]
minvalue=min(num([0]) #num 리스트의 0번에서 가장 작은 값=7저장 [비교의 기준]

for i in range(len(num)) : #리스트 길이만큼 반복

    print(i+1,"번째 줄의 합은:",sum(num[i]))

    if minvalue>min(num[i]) : #각 리스트의 최소값과 minvalue 비교
        minvalue=min(num[i])   
print("리스트에서 가장 작은 값:",minvalue)
