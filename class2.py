# class1.py 
#클래스정의(형식)
class Person:
    #클래스의 멤버변수 (주로 데이터를 공유)
    num_person=0
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
        Person.num_person+=1
    #인스턴스 메서드 
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성
p1 = Person()
p2 = Person()
p3 = Person()
print("인스턴스 개수 :", Person.num_person)

#클래스에 추가
Person.title = "new title"
print(Person.title)
print(p1.title)

#인스턴스에 추가
p1.age = 30
print(p1.age)
print(p2.age)