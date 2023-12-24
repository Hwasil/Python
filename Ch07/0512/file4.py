'''
05.12
파일 입출력(줄단위 입출력)
'''

L1=['충청', '충북\n', '강원', '강릉\n', '경남', '경북']
L2=[1,2,3,4,5]

with open('D:/Python_EX/0512/list.txt','w') as f:
    f.writelines(L1)