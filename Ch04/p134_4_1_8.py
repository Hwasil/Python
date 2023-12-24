'''이중 if(if~else)'''
first_num=int(input("첫 번째 숫자 입력 :"))
sceond_num=int(input("두 번째 숫자 입력 :"))

if first_num>sceond_num :
    print("두 숫자 중에 큰 수는 {}이고 작은 수는 {}이다.".format(first_num, sceond_num))

else:
     print("두 숫자 중에 큰 수는 {}이고 작은 수는 {}이다.".format(sceond_num, first_num))