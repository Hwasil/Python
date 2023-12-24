'''
0513 과제
members.txt(작성), reprot2.txt(생성)
'''

f=open("D:\\Python_EX\\0513_과제\\members.txt",'r')
read=f.readlines() 

for member in read : 
    memberlist=member.split(',') 

    name=memberlist[0]

for i in range(5) :
    if (memberlist[1]=="학생") :
        amount=15000
    
    elif (memberlist[1]=="교수") :
        amount=30000

    elif (memberlist[1]=="직원") :
        amount=30000

    elif (memberlist[1]=="일반") :
        amount=50000
    
    i=i+1

sum=0
for j in range(5) :
    sum=amount*memberlist[2]
    i=i+1

print(name+" : 등록금액",sum)
txts=f.read()
f.close()

f=open("D:\\Python_EX\\0513_과제\\report2.txt",'w')
f.write(txts) 
f.close()