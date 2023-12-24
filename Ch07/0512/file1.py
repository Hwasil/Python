'''
0512 파일 입출력
'''

f=open("D:\\Python_EX\\0512\\test.txt", "w")

for i in range(1,11) :
    f.write("%d번째 줄입니다\n"%i) 

f.close()