'''
0527
냉면 가격 계산
sales.txt/total_sales.txt
'''

market_write=open('D:\\Python_EX\\0527\\sales.txt','w') #테이블 별 냉면 판매 그릇 수 
price_write=open('D:\\Python_EX\\0527\\total_sales.txt','w') # 테이블 당 총 판매 금액 저장

food=0 # 냉면 그릇 수를 저장할 변수
table={1:0,2:0,3:0,4:0,5:0} #테이블 당 냉면 그릇 수 
total_price=0 #판매 금액의 합계

while True :
    select_table=int(input("테이블 번호 입력(1~5, 끝:0) :")) #테이블 번호 선택
    if select_table==0 : #반복문 종료
        print("영업종료")
        break
    food=int(input("그릇 수 입력 :"))
    table[select_table] += food #테이블 번호와 그릇 수 연결

    market_write.write(str(select_table)+" "+str(food)+'\n')
market_write.close()

for i in range(1,len(table)+1) :
    price=table[i]*7500 # 냉면 판매 금액
    price_write.write("%d 테이블 매출 : "%i + str(price)+'\n')
    total_price += price

price_write.write("오늘의 총 매출 : %d"%total_price)
price_write.close()