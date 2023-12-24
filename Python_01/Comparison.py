print('------큰 수 출력하기')
num = int(input("첫 번째 정수 >> "))
num2 = int(input("두 번째 정수 >> "))

if ( num < num2 ) :
    #print("입력한 두 정수 중 큰 수는 ", num2)
    max = num2
elif ( num == num2 ) :
    print("입력한 두 정수가 같습니다.")
else :
    #print("입력한 두 정수 중 큰 수는", num)
    max = num
    
print("입력한 두 정수 중 큰 수는", max)