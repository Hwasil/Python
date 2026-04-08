#26.04.08
# 클래스
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_score(self):
        print(self.name, self.score)
