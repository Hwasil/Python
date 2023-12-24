'''
05.12
파일 입출력(줄단위 입출력)
'''

with open('D:/Python_EX/0512/list.txt','r') as f:
    for line in f:
        print(line,end=' ')