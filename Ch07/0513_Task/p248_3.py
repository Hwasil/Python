'''
0513 과제
score1.txt(작성), 화면과 report1.txt(프로그램에서 생성) 파일에 출력
'''

f=open("D:\\Python_EX\\0513_과제\\score1.txt",'r')
lines=f.readlines()

for score in lines :
    scorelist=score.split()

    name=scorelist[0]

for i in range(4) :
    if scorelist[1]>90 :
        print(name+"A")

    elif 80<scorelist[1]<89 :
        print(name+"B")

    elif 70<scorelist[1]<79 :
        print(name+"C")

    elif 60<scorelist[1]<69 :
        print(name+"D")

    else :
        print(name+"E")

    i=i+1

txts=f.read()
f.close()

f=open("D:\\Python_EX\\0513_과제\\report1.txt",'w')
f.write(txts) 
f.close()