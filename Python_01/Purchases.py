import math

def size(shirt_size) :                  # 함수 정의 : 콜론, 함수 호출 시 ; 세미콜론 사용
    size_count = [0 for _ in range(6)]  # 초기값은 0으로 해서 총 6개 리스트 생성 
    
    for ss in shirt_size :              # 반복문으로 shirt_size 문자를 한 개씩 가져와서 비교
        if ss == "XS" :
            size_count[0] += 1
        elif ss == "S" :
            size_count[1] += 1
        elif ss == "M" :
            size_count[2] += 1
        elif ss == "L" :
            size_count[3] += 1
        elif ss == "XL" :
            size_count[4] += 1
        elif ss == "XXL" :
            size_count[5] += 1
    return size_count


shirt_size = ["XS", "S", "L", "L", "XL", "S"]   # 주문한 리스트 
ret = size(shirt_size);                         # 함수 호출

print("수량 조사 >> ", ret)