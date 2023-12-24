'''
0512 
파일 입출력/ readline() 한줄씩 읽어 들이는 메소드
'''

with open('D:/Python_EX/0512/list.txt','r') as f:

    while True :
        line=f.readline()
        print(line,end=' ')

        if line=="" : #공백
            break

