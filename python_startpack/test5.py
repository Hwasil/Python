# 클래스
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_score(self):
        print(self.name, self.score)


class Person:  # class로부터 찍어서 생성해 나온 것 -> 객체, 인스턴스
    def __init__(self, name, age, height):  # 생성자
        self.name = name
        self.age = age
        self.height = height

    def run():  # 객체이름.메서드로 호출
        pass
