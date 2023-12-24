print("-------------factorial!")
num = int(input("정수 입력 >> "))
total = 1

for i in range(1, num+1) :
    total = total * i
    
print(num, "!은 ", total, "이다.")