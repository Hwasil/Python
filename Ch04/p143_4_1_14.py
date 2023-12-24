"""복합 조건 프로그램"""
sex=input("당신의 성별은('M or m' 또는 'F or f'):")
height=float(input("키(cm) 입력:"))/100 #입력은 cm이지만 키를 m로 계산 
weight=float(input("몸무게(kg) 입력:"))

if (sex=='M' or sex=='m') :
    avg=height*height*22
    if (110<=weight/avg*100<=119) : #weight/avg*100 이거 무슨 의미지?
        print("과체중")
    elif (weight/avg*100>=120) :
        print("비만체중")
    else : 
        print("표준체중")

elif (sex=='F' or sex=='f') :
    height*height*21
    if (110<=weight/avg*100<=119) :
            print("과체중")
    elif (weight/avg*100>=120) :
        print("비만체중")
    else : 
        print("표준체중")

else : 
    print("성별을 잘못 입력하였습니다.")

