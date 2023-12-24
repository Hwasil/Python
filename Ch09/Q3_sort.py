'''
0610
문제 3
로또 복권 추첨 프로그램
'''

print('로또 프로그램 시작')

import random
lotto=[] # 빈리스트 생성

while True :
    a=(random.randint(1,45)) 

    if a not in lotto:
        lotto.append(a)
        lotto.sort()

# 중복 불가, 오름차순 정렬
    if len(lotto)==6 :
        print(lotto)
        break