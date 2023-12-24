'''
p209-5
'''
tup=(1,2,4,4,2,3,7,7,9,3)
print("최초의 튜플 :",tup)

not_list=[]

for i in range(len(tup)) :
    if tup[i] not in not_list : 
        print(tup[i],"개수 :",tup.count(tup[i]))
        not_list.append(tup[i])