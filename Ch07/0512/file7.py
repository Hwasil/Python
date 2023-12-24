'''
0512 
파일 입출력/ readlines() 한꺼번에 읽어 들이는 메소드
'''

with open('D:/Python_EX/0512/list1.txt','r') as f: 

    texts=f.readlines()

    print(type(texts))
    print(texts)