'''
0513 과제
score.txt(작성), report.txt(프로그램에서 생성)
'''

f=open("D:\\Python_EX\\0513_과제\\score.txt",'r')

lines=f.readlines() #파일로부터 모든 줄을 읽어 리스트 객체를 반환

for score in lines : #리스트 객체의 각 항목을 반복
    scorlist=score.split() #스페이스를 기준으로 리스트 객체로 반환
    name=scorlist[0] #첫 번째 항목을 이름으로 설정

    sum=0

    for i in range(1,3) :
        sum=sum+int(scorlist[i])
    print(name,'총점 :',sum,"평균",sum/3)
    
    txts=f.read() #파일의 모든 내용을 txts에 저장
f.close()

f=open("D:\\Python_EX\\0513_과제\\report.txt",'w')
f.write(txts) #txts 변수에 저장된 내용을 파일에 저장
f.close()