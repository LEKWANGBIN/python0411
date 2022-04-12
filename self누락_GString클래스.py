#파이썬은 명확하게 코딩하는 것이 좋다! 
#전역변수
str = "Not Class Member"
class GString:
    #초기화 메서드
    def __init__(self):
        #인스턴스 멤버변수
        self.str = "" 
    #세터(쓰기)
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그
        print(self.str)

#인스턴스 생성
g = GString()
g.set("First Message")
g.print()