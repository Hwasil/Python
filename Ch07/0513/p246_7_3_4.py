'''
0513
여러 문장 입력받아 txt에 저장
'''

enter=[]

while True :
    text=input("저장할 문장 입력(끝:엔터키) :")

    if text=="":
        break

    enter.append(text+"\n")

print("입력될 리스트 :",enter)

f=open("D:\\Python_EX\\0513\\out.txt",'w')
f.writelines(enter)
f.close()

print("out.txt 파일이 생성되었습니다.")
