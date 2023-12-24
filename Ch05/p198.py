'''
0429 p198
다중 리스트
'''
num=[[11,12,13],[21,22,23],[31,32,33],[41,42]]

for i in range(len(num)) : #리스트 길이 만큼 반복
    sum=0
    for j in range(len(num[i])) :
        sum=sum+num[i][j]
    print(i+1,"번째 줄의 합계:",sum)
