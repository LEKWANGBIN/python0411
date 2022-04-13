# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    #내가 원하는 값을 받아서 바로 인스턴스를 생성
    def __init__(self, id, name, balance):
        #인스턴스 멤버 변수 초기화
        self.id = id
        self.name = name 
        self.balance = balance 
    def deposit(self, amount):
        #입금
        self.balance += amount 
    def withdraw(self, amount):
        #출금
        self.balance -= amount
    #선택한 영역을 주석: ctrl + / (cmd + / )
    def __str__(self):
        #인스턴스의 문자열을 출력(ToString())
        return "{0}, {1}, {2}".format(self.id, 
        self.name, self.balance)

#인스턴스 객체를 생성
#디버깅(중단점, Break Point)
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1)