'''
0610
문제 1
친구와 전화번호 등록 후 
친구 이름으로 검색하면 전화번호 출력
'''

dict1={} # 빈 사전

while True :
    num=int(input('1) 친구 등록 2) 검색 3) 종료 :'))

    if num==1 :
        name=input("name :")
        phone=input("phone :")
        dict1[name]=phone
        
    elif num==2 :
        name=input('name :')
        
        if name in dict1 :
            print(dict1[name])

        elif name not in dict1 :
            print('Not Found')
    
    else : # 3
        break