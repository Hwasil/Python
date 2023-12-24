"""Binary Search"""
alist = [1, 3, 5, 6, 7, 9, 11, 20, 30, 56]

# 인덱스값
low = 0
hight = len(alist) - 1
result = False

find = int(input("탐색하고자 하는 값 >> "))

while result == False : # low <= hight and not result
    mid = (low + hight)//2

    if ( alist[mid] == find ) :
        result = True   # 무한루프 종료
    elif ( low > hight ) :
        break
    elif ( find < alist[mid]) :
        hight = mid - 1
    elif ( find > alist[mid]) :
        low = mid + 1 

print(result)