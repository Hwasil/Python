"""and"""
price=56000
surtax=0.1
total_price=price+(price*surtax)

print("음식요금이",price,"인 10% 부가세를 포함한 총 식사금액:",'%.0f'%total_price)
# 소수점 없애는 방법 : '%.0(소수이하 자릿수)f'%소수점 2자리 받을 값