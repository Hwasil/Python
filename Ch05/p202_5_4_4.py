'''
0429
다중 2차원 리스트, 학생의 총점은 학번과 같은 열에 있는 점수 3개의 합 출력
'''
num=[[2020001,2019002,2019003,2019004,2020005],[89,74,88,99,95],[91,75,68,98,88],[79,94,68,94,92]]
j=0 #학생 수가 적혀 있는 리스트

for s in range(len(num[0])) : #학생 수 만큼 반복, s는 학생 번호 수 
	print(num[j][s],"학생의 총점은:",num[j+1][s]+num[j+2][s]+num[j+3][s])