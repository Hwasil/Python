'''내포된 if문'''
score=int(input("점수를 입력하세요 :"))

if score>=60:
    if score>=70:
        if score>=80:
            if score>=90:
                print("A학점입니다.")
            else:
                print("B학점입니다.")
        else:
             print("C학점입니다.")
    else:
         print("D학점입니다.")
else:
    print("F학점입니다.")