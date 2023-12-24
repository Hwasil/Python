"""
key1 = "ABCDEFG"
key2 = "123456789"

#1
pw = key1[ :3] + key2[-4: ]
result = pw[-5:5]

#2
result = key1[1:4] + key2[-3:-1]

print(result)
"""

#3
a=0

for i in range(10, 4, -1) :
    if i%2 == 0:
        a = i
        print(a)

#4
n = 1
c = "v"

while True :
    print(c*n, end=" ") # v*2 => 2번 반복
    n += 1

    if n == 7:
        break

print(c*n)  # 마지막 출력