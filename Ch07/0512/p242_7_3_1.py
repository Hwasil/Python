'''
0512
p242 7-3-1 
파일 복사
'''

source=input("source 파일 입력 :")
target=input("target 파일 입력 :")

with open (source,'r') as f1:
    texts=f1.read()

with open (target,'w') as f2:
    f2.write(texts)

    print(target+"파일이 생성되었습니다.")