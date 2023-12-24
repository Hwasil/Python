print("--------------369 game!(배수 찾기)")
mul = int(input("숫자 입력 >> "))

for i in range(1, 101) :
    if ( i % mul == 0) :
        print("박수", end=" ")
    else :
        print(i, end=" ")