# 메모리관리.py 
#클래스를 정의(메모리 관리를 자동으로 처리):GC(가비지 컬렉션 서비스)
class MyClass:
    #초기화메서드(가장 먼저 실행)
    def __init__(self, value):
        self.value = value 
        print("Instance is created! value=", value)
    #인스턴스를 소멸할 때(가장 나중에 실행)
    def __del__(self):
        print("Instance is deleted!")

#인스턴스를 생성
d = MyClass(5)
#필요없으면 소멸
#del d 

print("---전체 코드 실행 종료---")