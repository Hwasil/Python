'''
21.05.06
'''

import random

lotto=set()
cnt=0 #랜덤 수 생성 개수 

while True :
    lotto.add(random.randint(1,45))
    cnt=cnt+1

    if len(lotto)==6 :
        break

print("이번 주 로또 번호 :",sorted(lotto))
print("중복도니 난수의 발생 횟수 :",cnt-6)