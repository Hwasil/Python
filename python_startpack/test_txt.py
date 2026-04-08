# 26.04.08
# 다섯 명의 학생 : 이름과 성적(국, 영, 수) 입력 받아 텍스트 파일에 저장
# 텍스트 파일에서 읽어와서 해당 학생의 성적 평군, 최고 성적 새 파일에 저장

# 입력 및 파일 저장
students = {}

for i in range(5):
    name = input("Name : ")
    kor = int(input("kor : "))
    eng = int(input("eng : "))
    math = int(input("math : "))

    score = {"kor": kor, "eng": eng, "math": math}
    students[name] = score
print(students)

with open("C:\\Users\\user\\OneDrive\\Desktop\\new\\students.txt", "w") as f:
    for k, v in students.items():
        print(k, v)
        data = f"{k}, {v}\n"
        f.write(data)

out_students = {}  # txt 파일에 읽어서 학생 저장

with open("C:\\Users\\user\\OneDrive\\Desktop\\new\\students.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        s = line.split("")  # 공백 기준으로 나눠서 각각 리스트에 저장
        name = s[0].strip()  # 학생 이름
        score = s[1]  # 학생 성적
        score = score.rstrip("\n")
        score = score.rstrip("}")
        items = score.split(",")

        d = {}

        for item in items:
            k, v = item.split(":")
            k = k.strip("'")
            d[k] = int(v)

        out_students[name] = d

print(out_students)

# 학생 평균, 최고점 계산
